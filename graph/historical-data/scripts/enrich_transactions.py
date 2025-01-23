import json
import requests
import os
import glob
from datetime import datetime
from typing import Dict, List, Optional
from tqdm import tqdm

class SubgraphDataEnricher:
    def __init__(self):
        self.endpoints = {
            'ethereum': 'https://api.studio.thegraph.com/query/66740/historical-data/v0.0.3',
            'base': 'https://api.studio.thegraph.com/query/66740/historical-data-base/v0.0.1',
            'sonic': 'https://api.studio.thegraph.com/query/66740/historical-data-sonic/v0.0.1'
        }
        self.session = requests.Session()
        
    def query_subgraph(self, chain: str, query: str, retries: int = 3) -> Optional[Dict]:
        """Execute a GraphQL query against the specified chain's subgraph with retries."""
        if chain not in self.endpoints:
            print(f"Unsupported chain: {chain}")
            return None
            
        for attempt in range(retries):
            try:
                response = self.session.post(
                    self.endpoints[chain],
                    json={'query': query},
                    timeout=10
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == retries - 1:
                    print(f"Error querying {chain} subgraph after {retries} attempts: {str(e)}")
                    return None
                print(f"Attempt {attempt + 1} failed, retrying...")
                continue
            except Exception as e:
                print(f"Unexpected error querying {chain} subgraph: {str(e)}")
                return None

    def get_eth_price_at_block(self, chain: str, block_number: int) -> Optional[float]:
        """Get ETH price in USD at a specific block number."""
        query = """
        {
            bundle(id: "1", block: { number: %d }) {
                ethPrice
            }
        }
        """ % block_number
        
        result = self.query_subgraph(chain, query)
        if result and 'data' in result and result['data']['bundle']:
            return float(result['data']['bundle']['ethPrice'])
        return None

    def get_token_data_at_block(self, chain: str, token_address: str, block_number: int) -> Optional[Dict]:
        """Get token price and volume data at a specific block number."""
        query = """
        {
            token(id: "%s", block: { number: %d }) {
                id
                symbol
                name
                decimals
                derivedETH
                totalSupply
                volume
                volumeUSD
                untrackedVolumeUSD
                txCount
                totalLiquidity
                priceUSD
                feesUSD
                poolCount
            }
            pairs(where: { token0: "%s" }, first: 5, block: { number: %d }) {
                id
                token0Price
                token1Price
                volumeUSD
                reserve0
                reserve1
                liquidityProviderCount
            }
        }
        """ % (token_address.lower(), block_number, token_address.lower(), block_number)
        
        result = self.query_subgraph(chain, query)
        if not result or 'data' not in result:
            return None
            
        data = result['data']
        token_data = data['token']
        pairs_data = data['pairs']
        
        if token_data:
            token_data['pairs'] = pairs_data
        return token_data

    def calculate_usd_values(self, tx: Dict, token_data: Dict, eth_price: float) -> Dict:
        """Calculate USD values for the transaction."""
        amount = float(tx['transaction']['amount'])
        eth_value = float(token_data.get('derivedETH', 0))
        
        return {
            'amount_usd': amount * eth_value * eth_price if eth_value and eth_price else None,
            'token_price_usd': eth_value * eth_price if eth_value and eth_price else None,
            'eth_price_usd': eth_price,
            'gas_cost_usd': (int(tx['transaction']['gas_used']) * int(tx['transaction']['gas_price']) / 1e18) * eth_price
        }

    def enrich_transactions(self, transactions_file: str) -> Dict:
        """Enrich transaction data with historical price and volume data."""
        # Load transaction data
        try:
            with open(transactions_file, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file {transactions_file}: {str(e)}")
            raise
        except Exception as e:
            print(f"Error opening file {transactions_file}: {str(e)}")
            raise
            
        enriched_data = {
            'wallet_address': data['wallet_address'],
            'timestamp': data['timestamp'],
            'total_transactions': data['total_transactions'],
            'transactions_by_chain': {}
        }
        
        # Process each chain's transactions
        for chain, transactions in data['transactions_by_chain'].items():
            print(f"\nProcessing {chain} transactions...")
            enriched_transactions = []
            
            # Create progress bar for this chain's transactions
            with tqdm(total=len(transactions), desc=f"{chain.title()} Progress") as pbar:
                for tx in transactions:
                    try:
                        # Get ETH price at transaction block
                        eth_price = self.get_eth_price_at_block(chain, tx['transaction']['block_number'])
                        
                        # Get token data at transaction block
                        token_data = self.get_token_data_at_block(
                            chain,
                            tx['transaction']['token']['contract'],
                            tx['transaction']['block_number']
                        )
                        
                        # Enrich transaction with token data
                        enriched_tx = tx.copy()
                        if token_data:
                            # Calculate USD values
                            usd_values = self.calculate_usd_values(tx, token_data, eth_price)
                            
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
                                'top_pairs': [{
                                    'pair_address': pair['id'],
                                    'token0_price': pair['token0Price'],
                                    'token1_price': pair['token1Price'],
                                    'volume_usd': pair['volumeUSD'],
                                    'reserve0': pair['reserve0'],
                                    'reserve1': pair['reserve1'],
                                    'lp_count': pair['liquidityProviderCount']
                                } for pair in token_data.get('pairs', [])]
                            }
                            enriched_tx['usd_values'] = usd_values
                            
                        enriched_transactions.append(enriched_tx)
                        pbar.update(1)
                        
                    except Exception as e:
                        print(f"\nError processing transaction in {chain}: {str(e)}")
                        enriched_transactions.append(tx)  # Keep original transaction on error
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