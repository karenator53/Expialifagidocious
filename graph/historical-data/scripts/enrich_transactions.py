import json
import requests
import os
import glob
from datetime import datetime
import time
from typing import Dict, List, Optional, Set
from tqdm import tqdm

class SubgraphDataEnricher:
    def __init__(self):
        # Update endpoints to use production URLs with correct subgraph IDs
        self.endpoints = {
            # 'ethereum': 'https://gateway.thegraph.com/api/de5f9271c76a8aef76d0fd256d2c5b7d/subgraphs/id/3NDxoN5yx98c1Kch8Z6vhtjcAJqQckhfbFEwNYWZMFZd',
            # 'base': 'https://gateway.thegraph.com/api/de5f9271c76a8aef76d0fd256d2c5b7d/subgraphs/id/61B4py85G5mC2LzLg6CVnMzjqRoiPcmnnEmmqER7oKDu',
            'sonic': 'https://api.studio.thegraph.com/query/102096/historical-data-sonic/0.0.7'  # Updated to correct Sonic endpoint
        }
        # Initialize session with recommended headers from The Graph docs
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'GraphQL-Client',
            'Accept': 'application/json'
        })
        # Rate limiting parameters
        self.request_times = []
        self.rate_limit = 25  # requests per second
        self.rate_window = 1.0  # seconds
        # Retry parameters - reduced to 1
        self.max_retries = 1
        self.base_delay = 1.0
        self.max_delay = 30.0
        # Initialize block ranges as empty, will be fetched dynamically
        self.block_ranges = {}
        # Add delay between retries
        self.retry_delay = 1.0
        
    def format_address(self, address: str) -> str:
        """Format address to match subgraph's hex string format."""
        # Remove '0x' prefix if present and convert to lowercase
        clean_addr = address.lower().replace('0x', '')
        # Add '0x' prefix back
        return f"0x{clean_addr}"

    def get_chain_block_range(self, chain: str) -> Dict[str, int]:
        """Query the subgraph to get the actual block range using multiple methods."""
        # First try the _meta query
        meta_query = """
        {
            _meta {
                block {
                    number
                }
                deployment
                hasIndexingErrors
                features
            }
        }
        """
        
        # Also try to get the earliest and latest blocks with data
        range_query = """
        {
            tokens(first: 1, orderBy: createdAtBlockNumber, orderDirection: asc) {
                createdAtBlockNumber
            }
            _meta {
                block {
                    number
                }
            }
        }
        """
        
        result = self.query_subgraph(chain, range_query)
        if result and 'data' in result:
            meta = result['data'].get('_meta', {})
            tokens = result['data'].get('tokens', [])
            
            latest_block = meta.get('block', {}).get('number', 0)
            start_block = tokens[0].get('createdAtBlockNumber', 0) if tokens else 0
            
            # Start block is 1 for all chains
            start_block = 1
                
            return {'start': start_block, 'end': latest_block}
            
        return {'start': 0, 'end': float('inf')}

    def update_range_from_error(self, chain: str, error_msg: str):
        """Update block range based on error message with better parsing."""
        try:
            if 'before minimum `startBlock` of manifest' in error_msg:
                start_block = int(error_msg.split('startBlock` of manifest ')[1].strip())
                current = self.block_ranges.get(chain, {'start': 0, 'end': float('inf')})
                self.block_ranges[chain] = {
                    'start': max(current['start'], start_block),
                    'end': current['end']
                }
            elif 'missing block' in error_msg and 'latest' in error_msg:
                # Extract both the requested block and latest block
                parts = error_msg.split('missing block: ')[1].split(', latest: ')
                if len(parts) == 2:
                    requested_block = int(''.join(c for c in parts[0] if c.isdigit()))
                    latest_block = int(''.join(c for c in parts[1] if c.isdigit()))
                    current = self.block_ranges.get(chain, {'start': 0, 'end': float('inf')})
                    self.block_ranges[chain] = {
                        'start': current['start'],
                        'end': min(current['end'], latest_block)
                    }
                    print(f"Updated {chain} block range: start={self.block_ranges[chain]['start']}, end={self.block_ranges[chain]['end']}")
                    print(f"Note: Requested block {requested_block} is beyond the latest indexed block {latest_block}")
        except Exception as e:
            print(f"Error updating block range from message: {str(e)}")

    def wait_for_rate_limit(self):
        """Implement token bucket rate limiting."""
        now = time.time()
        # Remove old requests outside the window
        self.request_times = [t for t in self.request_times if now - t < self.rate_window]
        
        if len(self.request_times) >= self.rate_limit:
            # Wait until we can make another request
            sleep_time = self.request_times[0] + self.rate_window - now
            if sleep_time > 0:
                time.sleep(sleep_time)
            self.request_times = self.request_times[1:]
        
        self.request_times.append(now)

    def query_subgraph(self, chain: str, query: str, variables: Dict = None) -> Optional[Dict]:
        """Execute a GraphQL query with variables support."""
        if chain not in self.endpoints:
            print(f"Unsupported chain: {chain}")
            return None
            
        try:
            self.wait_for_rate_limit()
            
            request_data = {'query': query}
            if variables:
                request_data['variables'] = variables
            
            response = self.session.post(
                self.endpoints[chain],
                json=request_data,
                timeout=30
            )
            
            if response.status_code == 429:
                print(f"Rate limited on {chain}")
                return None
                
            response.raise_for_status()
            result = response.json()
            
            if 'errors' in result:
                errors = result['errors']
                error_messages = [error.get('message', '') for error in errors]
                print(f"\nGraphQL errors for {chain}:")
                for msg in error_messages:
                    print(f"- {msg}")
                return None
            
            return result
            
        except Exception as e:
            print(f"Error querying {chain}: {str(e)}")
            return None

    def update_block_ranges(self):
        """Update block ranges for all chains."""
        print("\nUpdating block ranges from subgraphs...")
        for chain in self.endpoints.keys():
            print(f"Querying {chain} block range...")
            self.block_ranges[chain] = self.get_chain_block_range(chain)
            print(f"- {chain}: blocks {self.block_ranges[chain]['start']} to {self.block_ranges[chain]['end']}")
            
    def filter_blocks_in_range(self, chain: str, block_numbers: Set[int]) -> Set[int]:
        """Filter block numbers based on chain-specific constraints."""
        if not block_numbers:
            return set()
            
        min_block = min(block_numbers)
        max_block = max(block_numbers)
        
        # No minimum block constraints needed
        return block_numbers

    def get_block_data(self, chain: str, token_addresses: Set[str], block_numbers: Set[int]) -> Dict:
        """Get token and price data for multiple blocks in a single query."""
        if not block_numbers:
            print(f"No blocks provided for {chain}")
            return {}
            
        if chain not in self.endpoints:
            print(f"Chain {chain} not enabled")
            return {}

        # Convert addresses to proper format
        formatted_addresses = {self.format_address(addr) for addr in token_addresses}

        # First get all available tokens from the subgraph
        tokens_query = """
        {
            tokens(first: 1000) {
                id
                symbol
                name
                totalValueLockedUSD
                txCount
            }
            pairs(first: 100, orderBy: reserveUSD, orderDirection: desc) {
                token0 { id }
                token1 { id }
            }
            pools(first: 100, orderBy: volumeUSD, orderDirection: desc) {
                token0 { id }
                token1 { id }
            }
        }
        """
        
        tokens_result = self.query_subgraph(chain, tokens_query)
        if not tokens_result or 'data' not in tokens_result:
            print("\nFailed to fetch available tokens")
            return {}

        # Collect token IDs from all sources
        available_tokens = {}
        
        # Direct tokens
        for token in tokens_result['data'].get('tokens', []):
            token_id = token['id'].lower()
            available_tokens[token_id] = token.get('symbol', 'Unknown')
            
        # Tokens from pairs
        for pair in tokens_result['data'].get('pairs', []):
            if pair.get('token0'):
                token_id = pair['token0']['id'].lower()
                if token_id not in available_tokens:
                    available_tokens[token_id] = 'Unknown'
            if pair.get('token1'):
                token_id = pair['token1']['id'].lower()
                if token_id not in available_tokens:
                    available_tokens[token_id] = 'Unknown'
                    
        # Tokens from pools
        for pool in tokens_result['data'].get('pools', []):
            if pool.get('token0'):
                token_id = pool['token0']['id'].lower()
                if token_id not in available_tokens:
                    available_tokens[token_id] = 'Unknown'
            if pool.get('token1'):
                token_id = pool['token1']['id'].lower()
                if token_id not in available_tokens:
                    available_tokens[token_id] = 'Unknown'

        print(f"\nFound {len(available_tokens)} total tokens in subgraph")
        
        # Check which of our tokens exist
        matching_tokens = {addr: available_tokens[addr] 
                         for addr in formatted_addresses 
                         if addr in available_tokens}
        
        print("\nToken matching results:")
        print(f"- Input tokens: {len(formatted_addresses)}")
        print(f"- Matching tokens: {len(matching_tokens)}")
        
        if matching_tokens:
            print("\nMatched tokens:")
            for addr, symbol in matching_tokens.items():
                print(f"- {symbol} ({addr})")
        else:
            print("\nNo matching tokens found. Input tokens:")
            for addr in formatted_addresses:
                print(f"- {addr}")
            return {}

        # Now proceed with block data query using matched tokens
        query = """
        query GetBlockData($blockNumber: Int!, $tokenIds: [String!]!) {
            tokens(
                where: { id_in: $tokenIds }
                block: { number: $blockNumber }
            ) {
                id
                symbol
                name
                decimals
                derivedETH
                totalValueLockedUSD
                volume
                volumeUSD
                untrackedVolumeUSD
                txCount
            }
            pairs(
                first: 100
                orderBy: volumeUSD
                orderDirection: desc
                block: { number: $blockNumber }
            ) {
                id
                token0 { id }
                token1 { id }
                reserve0
                reserve1
                reserveUSD
                volumeToken0
                volumeToken1
                volumeUSD
            }
        }
        """
        
        all_data = {}
        
        # Process blocks in batches
        BLOCK_BATCH_SIZE = 1
        block_batches = [list(block_numbers)[i:i+BLOCK_BATCH_SIZE] 
                        for i in range(0, len(block_numbers), BLOCK_BATCH_SIZE)]
        
        print(f"\nProcessing queries for {chain}:")
        print(f"- {len(block_batches)} block batches")
        print(f"- {len(matching_tokens)} tokens per query")
        
        for block_batch in block_batches:
            for block in block_batch:
                variables = {
                    "blockNumber": block,
                    "tokenIds": list(matching_tokens.keys())
                }
                
                result = self.query_subgraph(chain, query, variables)
                if result and 'data' in result:
                    # Store token data with block number
                    for token in result['data'].get('tokens', []):
                        token_id = token['id'].lower()
                        all_data[f't{token_id}_{block}'] = token
                    
                    # Store pair data
                    all_data[f'pairs_{block}'] = result['data'].get('pairs', [])
                    
                    # Add default bundle data
                    all_data[f'b{block}'] = {'ethPrice': '1.0'}
                else:
                    # If query fails, add empty data
                    for token_id in matching_tokens:
                        all_data[f't{token_id}_{block}'] = None
                    all_data[f'pairs_{block}'] = []
                    all_data[f'b{block}'] = {'ethPrice': '1.0'}
        
        return all_data

    def enrich_transactions(self, transactions_file: str) -> Dict:
        """Enrich transaction data with historical price and volume data."""
        try:
            with open(transactions_file, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file {transactions_file}: {str(e)}")
            raise
            
        enriched_data = {
            'wallet_address': data['wallet_address'],
            'timestamp': data['timestamp'],
            'total_transactions': data['total_transactions'],
            'transactions_by_chain': {}
        }
        
        # Process each chain's transactions
        for chain, transactions in data['transactions_by_chain'].items():
            # Skip chains that aren't in our endpoints
            if chain not in self.endpoints:
                print(f"\nSkipping {chain} chain - not currently enabled")
                continue
                
            print(f"\nProcessing {chain} transactions...")
            
            # Collect unique token addresses and block numbers
            token_addresses = {tx['transaction']['token']['contract'].lower() for tx in transactions}
            block_numbers = {tx['transaction']['block_number'] for tx in transactions}
            
            print(f"Found {len(token_addresses)} unique tokens and {len(block_numbers)} unique blocks")
            
            # Process in smaller batches
            BATCH_SIZE = 5  # Reduced batch size
            enriched_transactions = []
            
            with tqdm(total=len(transactions), desc=f"{chain.title()} Progress") as pbar:
                # Create a mapping of block numbers to transactions for efficient lookup
                block_to_txs = {}
                for tx in transactions:
                    block_num = tx['transaction']['block_number']
                    if block_num not in block_to_txs:
                        block_to_txs[block_num] = []
                    block_to_txs[block_num].append(tx)
                
                # Process blocks in batches
                for i in range(0, len(block_numbers), BATCH_SIZE):
                    block_batch = list(block_numbers)[i:i+BATCH_SIZE]
                    
                    # Get data for this batch
                    block_data = self.get_block_data(chain, token_addresses, set(block_batch))
                    
                    # Process all transactions in the current block batch
                    for block_num in block_batch:
                        if block_num not in block_to_txs:
                            continue
                            
                        for tx in block_to_txs[block_num]:
                            try:
                                token_addr = tx['transaction']['token']['contract'].lower()
                                
                                # Get ETH price and token data from the combined query results
                                eth_price = float(block_data.get(f'b{block_num}', {}).get('ethPrice', 0))
                                token_data = block_data.get(f't{token_addr}_{block_num}', {})  # Default to empty dict
                                pairs_data = block_data.get(f'pairs_{block_num}', [])  # Default to empty list
                                
                                # Enrich transaction
                                enriched_tx = tx.copy()
                                
                                # Only add token data if we have valid data
                                if token_data is not None:
                                    enriched_tx['token_data'] = {
                                        'price_eth': token_data.get('derivedETH'),
                                        'price_usd': token_data.get('priceUSD'),
                                        'total_supply': token_data.get('totalSupply'),
                                        'total_liquidity': token_data.get('totalLiquidity'),
                                        'volume': token_data.get('volume'),
                                        'volume_usd': token_data.get('volumeUSD'),
                                        'untracked_volume_usd': token_data.get('untrackedVolumeUSD'),
                                        'fees_usd': token_data.get('feesUSD'),
                                        'pool_count': token_data.get('poolCount'),
                                        'tx_count': token_data.get('txCount'),
                                        'top_pairs': pairs_data if pairs_data else []
                                    }
                                    
                                    # Only calculate USD values if we have valid price data
                                    eth_value = float(token_data.get('derivedETH', 0))
                                    if eth_value and eth_price:
                                        amount = float(tx['transaction']['amount'])
                                        gas_used = int(tx['transaction'].get('gas_used', 0))
                                        gas_price = int(tx['transaction'].get('gas_price', 0))
                                        
                                        enriched_tx['usd_values'] = {
                                            'amount_usd': amount * eth_value * eth_price,
                                            'token_price_usd': eth_value * eth_price,
                                            'eth_price_usd': eth_price,
                                            'gas_cost_usd': (gas_used * gas_price / 1e18) * eth_price if gas_used and gas_price else 0
                                        }
                                else:
                                    # Add empty data structures for consistency
                                    enriched_tx['token_data'] = {
                                        'price_eth': None,
                                        'price_usd': None,
                                        'total_supply': None,
                                        'total_liquidity': None,
                                        'volume': None,
                                        'volume_usd': None,
                                        'untracked_volume_usd': None,
                                        'fees_usd': None,
                                        'pool_count': None,
                                        'tx_count': None,
                                        'top_pairs': []
                                    }
                                    enriched_tx['usd_values'] = {
                                        'amount_usd': None,
                                        'token_price_usd': None,
                                        'eth_price_usd': eth_price,
                                        'gas_cost_usd': 0
                                    }
                                
                                enriched_transactions.append(enriched_tx)
                                pbar.update(1)
                                
                            except Exception as e:
                                print(f"\nError processing transaction in {chain}: {str(e)}")
                                enriched_transactions.append(tx)
                                pbar.update(1)
                                continue
            
            enriched_data['transactions_by_chain'][chain] = enriched_transactions
            
        return enriched_data

    def save_enriched_data(self, enriched_data: Dict, original_file: str) -> str:
        """Save enriched data to a new JSON file."""
        output_file = original_file.replace('.json', '_enriched.json')
        with open(output_file, 'w') as f:
            json.dump(enriched_data, f, indent=2)
        return output_file

def find_transaction_files() -> List[str]:
    """Find all transaction JSON files in the testdata directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    testdata_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))), "testdata")
    
    if not os.path.exists(testdata_dir):
        raise FileNotFoundError(f"testdata directory not found at {testdata_dir}")
        
    pattern = os.path.join(testdata_dir, "transactions_*.json")
    files = glob.glob(pattern)
    return [f for f in files if not f.endswith('_enriched.json')]

def format_usd(value: float) -> str:
    """Format USD value with appropriate suffix (K, M, B)."""
    if value >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value/1_000:.2f}K"
    return f"${value:.2f}"

def main():
    print("Transaction Data Enricher")
    print("This tool enriches transaction data with historical price and volume information.")
    
    try:
        # Initialize enricher
        enricher = SubgraphDataEnricher()
        
        # Find all transaction files
        transaction_files = find_transaction_files()
        if not transaction_files:
            print("No transaction files found in the testdata directory.")
            return
            
        print(f"\nFound {len(transaction_files)} transaction files to process:")
        for file in transaction_files:
            print(f"- {os.path.basename(file)}")
        
        # Process each file
        for file_path in transaction_files:
            try:
                print(f"\nProcessing: {os.path.basename(file_path)}")
                start_time = datetime.now()
                
                enriched_data = enricher.enrich_transactions(file_path)
                output_file = enricher.save_enriched_data(enriched_data, file_path)
                
                processing_time = datetime.now() - start_time
                print(f"\nEnriched data saved to: {os.path.basename(output_file)}")
                print(f"Processing time: {processing_time.total_seconds():.2f} seconds")
                
                # Print summary
                print("\nEnrichment Summary:")
                total_value_usd = 0.0
                total_gas_usd = 0.0
                
                for chain, transactions in enriched_data['transactions_by_chain'].items():
                    enriched_count = sum(1 for tx in transactions if 'token_data' in tx)
                    total_count = len(transactions)
                    
                    # Calculate totals
                    chain_value_usd = sum(
                        float(tx.get('usd_values', {}).get('amount_usd', 0) or 0)
                        for tx in transactions
                        if 'usd_values' in tx
                    )
                    chain_gas_usd = sum(
                        float(tx.get('usd_values', {}).get('gas_cost_usd', 0) or 0)
                        for tx in transactions
                        if 'usd_values' in tx
                    )
                    
                    total_value_usd += chain_value_usd
                    total_gas_usd += chain_gas_usd
                    
                    print(f"\n{chain.title()}:")
                    print(f"- Transactions: {enriched_count}/{total_count} enriched")
                    print(f"- Total Value: {format_usd(chain_value_usd)}")
                    print(f"- Total Gas: {format_usd(chain_gas_usd)}")
                
                print(f"\nPortfolio Summary:")
                print(f"- Total Value: {format_usd(total_value_usd)}")
                print(f"- Total Gas Spent: {format_usd(total_gas_usd)}")
                print(f"- Net Value: {format_usd(total_value_usd - total_gas_usd)}")
                
            except Exception as e:
                print(f"Error processing file {os.path.basename(file_path)}: {str(e)}")
                continue
                
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user. Partial results may have been saved.")
    except Exception as e:
        print(f"Fatal error: {str(e)}")

if __name__ == "__main__":
    main() 