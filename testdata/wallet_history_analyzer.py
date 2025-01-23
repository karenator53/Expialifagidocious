import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import time
from collections import defaultdict
from web3 import Web3
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WalletHistoryAnalyzer:
    def __init__(self):
        self.graph_key = "de5f9271c76a8aef76d0fd256d2c5b7d"
        self.testdata_dir = Path(__file__).parent
        self.price_cache = {}
        
        # Define the GraphQL query for historical trades
        self.trade_query = """
        query getHistoricalTrades($wallet: String!, $block: Int!) {
          swaps(
            where: {
              or: [
                { from: $wallet },
                { to: $wallet }
              ],
              blockNumber_lte: $block
            }
            orderBy: blockNumber
            orderDirection: desc
            first: 1000
          ) {
            id
            timestamp
            transaction {
              id
              blockNumber
            }
            pair {
              token0 {
                id
                symbol
                decimals
              }
              token1 {
                id
                symbol
                decimals
              }
              token0Price
              token1Price
            }
            amount0In
            amount1In
            amount0Out
            amount1Out
          }
        }
        """
        
        # Updated Graph endpoints for DEXes
        self.graph_endpoints = {
            'ethereum': {
                'uniswap_v2': 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
                'uniswap_v3': 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
            },
            'base': {
                'baseswap': 'https://api.studio.thegraph.com/query/48080/baseswap-v2/version/latest'
            },
            'sonic': {
                'sonicswap': 'https://api.studio.thegraph.com/query/48080/sonicswap-v2/version/latest'
            }
        }
        
        # Initialize session
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })
        
    def get_token_price_at_block(self, token_address: str, block_number: int, chain: str) -> Optional[float]:
        """Get historical token price using The Graph"""
        cache_key = (token_address, block_number, chain)
        if cache_key in self.price_cache:
            logger.debug(f"Using cached price for {token_address} at block {block_number}")
            return self.price_cache[cache_key]
            
        logger.info(f"\nAttempting to get price for {token_address} on {chain} at block {block_number}")
        
        # Handle stablecoins
        stablecoins = {
            "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48": 1.0,  # USDC
            "0xdac17f958d2ee523a2206206994597c13d831ec7": 1.0,  # USDT
            "0x6b175474e89094c44da98b954eedeac495271d0f": 1.0,  # DAI
        }
        if token_address.lower() in stablecoins:
            price = stablecoins[token_address.lower()]
            self.price_cache[cache_key] = price
            logger.info(f"Using fixed price ${price:.6f} for stablecoin {token_address}")
            return price
            
        # Check if we have endpoints for this chain
        if chain not in self.graph_endpoints:
            logger.error(f"No Graph endpoints configured for chain: {chain}")
            return None
            
        token_address = token_address.lower()
        prices = []
        
        # Try each DEX subgraph for the chain
        for dex, endpoint in self.graph_endpoints.get(chain, {}).items():
            logger.info(f"Querying {dex} on {chain}...")
            try:
                response = self.session.post(
                    endpoint,
                    json={
                        'query': self.trade_query,
                        'variables': {
                            'wallet': token_address,
                            'block': block_number
                        }
                    }
                )
                
                if response.status_code != 200:
                    logger.error(f"HTTP {response.status_code} from {dex}: {response.text}")
                    continue
                    
                data = response.json()
                if 'errors' in data:
                    logger.error(f"GraphQL errors from {dex}: {data['errors']}")
                    continue
                    
                # Log raw response for debugging
                logger.debug(f"Raw response from {dex}: {data}")
                
                # Process swaps where token is token0
                swaps = data.get('data', {}).get('swaps', [])
                logger.info(f"Found {len(swaps)} swaps on {dex}")
                
                for swap in swaps:
                    if swap.get('amount0In') and swap.get('amount0Out') and swap.get('amount0Out') > 0:
                        price = float(swap['pair']['token0Price'])
                        amount = float(swap['amount0Out']) - float(swap['amount0In'])
                        if price > 0:
                            prices.append((price, amount))
                            logger.info(f"Found price ${price:.6f} with amount {amount:.4f} from {dex} (token0)")
                    else:
                        logger.debug(f"Invalid swap data from {dex}: {swap}")
                        
                # Process swaps where token is token1
                swaps = data.get('data', {}).get('swaps', [])
                logger.info(f"Found {len(swaps)} swaps on {dex}")
                
                for swap in swaps:
                    if swap.get('amount1In') and swap.get('amount1Out') and swap.get('amount1Out') > 0:
                        price = float(swap['pair']['token1Price'])
                        amount = float(swap['amount1Out']) - float(swap['amount1In'])
                        if price > 0:
                            prices.append((price, amount))
                            logger.info(f"Found price ${price:.6f} with amount {amount:.4f} from {dex} (token1)")
                    else:
                        logger.debug(f"Invalid swap data from {dex}: {swap}")
                        
            except Exception as e:
                logger.error(f"Error querying {dex}: {str(e)}", exc_info=True)
                continue
        
        if prices:
            # Use TVL-weighted average price from all swaps
            total_amount = sum(amount for _, amount in prices)
            weighted_price = sum(price * amount for price, amount in prices) / total_amount
            self.price_cache[cache_key] = weighted_price
            logger.info(f"Final TVL-weighted price ${weighted_price:.6f} from {len(prices)} swaps")
            return weighted_price
            
        logger.error(f"No valid prices found for {token_address} at block {block_number} after trying all DEXes on {chain}")
        return None
        
    def load_transactions(self) -> List[Dict]:
        """Load all transaction files from the testdata directory"""
        transactions = []
        transaction_files = list(self.testdata_dir.glob('transactions_*.json'))
        
        if not transaction_files:
            raise FileNotFoundError(f"No transaction files found in {self.testdata_dir}")
            
        logger.info("\nLoading transaction files:")
        for file_path in transaction_files:
            logger.info(f"Processing {file_path.name}...")
            with open(file_path, 'r') as f:
                tx_data = json.load(f)
                transactions.append(tx_data)
        return transactions
        
    def analyze_wallet(self, transactions: List[Dict]) -> Dict:
        """Analyze wallet transactions with historical prices"""
        wallet_data = defaultdict(lambda: {
            'total_invested': 0.0,
            'total_realized': 0.0,
            'current_holdings': defaultdict(float),
            'tokens': defaultdict(lambda: {
                'buys': [],
                'sells': [],
                'current_balance': 0.0,
                'total_bought': 0.0,
                'total_sold': 0.0,
                'realized_pnl': 0.0,
                'cost_basis': 0.0,
                'avg_buy_price': 0.0
            })
        })
        
        for tx in transactions:
            for chain, chain_txs in tx.get('transactions_by_chain', {}).items():
                for tx_data in chain_txs:
                    if 'transaction' not in tx_data:
                        continue
                        
                    tx = tx_data['transaction']
                    token_address = tx['token']['contract'].lower()
                    amount = float(tx['amount'])
                    block_number = int(tx['block_number'])
                    wallet_address = tx['to'].lower() if tx['type'] == 'buy' else tx['from'].lower()
                    
                    # Get historical price
                    price = self.get_token_price_at_block(token_address, block_number, chain)
                    if price is None:
                        logger.warning(f"Could not get price for {tx['token']['symbol']} at block {block_number}")
                        continue
                        
                    trade = {
                        'timestamp': tx['timestamp'],
                        'amount': amount,
                        'price': price,
                        'value': amount * price,
                        'block': block_number,
                        'hash': tx['hash']
                    }
                    
                    wallet = wallet_data[wallet_address]
                    token = wallet['tokens'][token_address]
                    
                    if tx['type'] == 'buy':
                        token['buys'].append(trade)
                        token['total_bought'] += amount
                        
                        # Update average buy price
                        total_value = token['avg_buy_price'] * token['current_balance'] + trade['value']
                        new_balance = token['current_balance'] + amount
                        if new_balance > 0:
                            token['avg_buy_price'] = total_value / new_balance
                            
                        token['current_balance'] = new_balance
                        wallet['total_invested'] += trade['value']
                        token['cost_basis'] = token['avg_buy_price']  # Use average buy price as cost basis
                        
                    else:  # sell
                        token['sells'].append(trade)
                        if token['current_balance'] > 0:  # Only process sell if we have balance
                            realized_pnl = (price - token['cost_basis']) * min(amount, token['current_balance'])
                            token['realized_pnl'] += realized_pnl
                            wallet['total_realized'] += realized_pnl
                            token['total_sold'] += amount
                            token['current_balance'] -= amount
                            
                            # Keep cost basis if there's remaining balance, reset if zero
                            if token['current_balance'] <= 0:
                                token['current_balance'] = 0
                                token['cost_basis'] = 0
                                token['avg_buy_price'] = 0
                        else:
                            logger.warning(f"Attempted to sell {amount} tokens but balance is {token['current_balance']}")
                            
                    wallet['current_holdings'][token_address] = token['current_balance']
                    
        return wallet_data
        
    def generate_report(self, wallet_data: Dict):
        """Generate a detailed report of wallet activity"""
        report = {
            'generated_at': datetime.now().isoformat(),
            'wallets': {}
        }
        
        for wallet_address, wallet in wallet_data.items():
            wallet_report = {
                'address': wallet_address,
                'total_invested': wallet['total_invested'],
                'total_realized_pnl': wallet['total_realized'],
                'current_holdings': [],
                'token_history': []
            }
            
            for token_address, token in wallet['tokens'].items():
                if token['current_balance'] > 0:
                    wallet_report['current_holdings'].append({
                        'token_address': token_address,
                        'balance': token['current_balance'],
                        'cost_basis': token['cost_basis']
                    })
                    
                wallet_report['token_history'].append({
                    'token_address': token_address,
                    'total_bought': token['total_bought'],
                    'total_sold': token['total_sold'],
                    'realized_pnl': token['realized_pnl'],
                    'trades': {
                        'buys': token['buys'],
                        'sells': token['sells']
                    }
                })
                
            report['wallets'][wallet_address] = wallet_report
            
        # Save report
        output_file = self.testdata_dir / 'wallet_history.json'
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
            
        logger.info(f"\nReport saved to {output_file}")
        
        # Print summary
        for wallet_address, wallet_report in report['wallets'].items():
            print(f"\n{'='*80}")
            print(f"Wallet: {wallet_address}")
            print(f"{'='*80}")
            print(f"Total Invested: ${wallet_report['total_invested']:,.2f}")
            print(f"Total Realized PnL: ${wallet_report['total_realized_pnl']:,.2f}")
            print(f"\nCurrent Holdings:")
            for holding in wallet_report['current_holdings']:
                print(f"  {holding['token_address']}: {holding['balance']:,.4f} tokens (Cost Basis: ${holding['cost_basis']:,.6f})")
            print("\nToken History:")
            for token in wallet_report['token_history']:
                print(f"\n  {token['token_address']}:")
                print(f"    Total Bought: {token['total_bought']:,.4f}")
                print(f"    Total Sold: {token['total_sold']:,.4f}")
                print(f"    Realized PnL: ${token['realized_pnl']:,.2f}")

    def get_historical_trades(self, wallet_address: str, block_number: int, chain: str) -> List[Dict]:
        """Get historical trades for a wallet up to a specific block"""
        trades = []
        wallet_address = wallet_address.lower()
        
        logger.info(f"\nFetching historical trades for {wallet_address} on {chain} up to block {block_number}")
        
        for dex, endpoint in self.graph_endpoints.get(chain, {}).items():
            logger.info(f"Querying {dex}...")
            try:
                response = self.session.post(
                    endpoint,
                    json={
                        'query': self.trade_query,
                        'variables': {
                            'wallet': wallet_address,
                            'block': block_number
                        }
                    }
                )
                
                if response.status_code != 200:
                    logger.error(f"HTTP {response.status_code} from {dex}: {response.text}")
                    continue
                    
                data = response.json()
                if 'errors' in data:
                    logger.error(f"GraphQL errors from {dex}: {data['errors']}")
                    continue
                    
                swaps = data.get('data', {}).get('swaps', [])
                logger.info(f"Found {len(swaps)} swaps on {dex}")
                
                for swap in swaps:
                    trade = {
                        'timestamp': int(swap['timestamp']),
                        'block': int(swap['transaction']['blockNumber']),
                        'tx_hash': swap['transaction']['id'],
                        'pair_address': swap['pair']['id'],
                        'token0': {
                            'address': swap['pair']['token0']['id'],
                            'symbol': swap['pair']['token0']['symbol'],
                            'decimals': int(swap['pair']['token0']['decimals'])
                        },
                        'token1': {
                            'address': swap['pair']['token1']['id'],
                            'symbol': swap['pair']['token1']['symbol'],
                            'decimals': int(swap['pair']['token1']['decimals'])
                        },
                        'amount0In': float(swap['amount0In']),
                        'amount1In': float(swap['amount1In']),
                        'amount0Out': float(swap['amount0Out']),
                        'amount1Out': float(swap['amount1Out']),
                        'token0Price': float(swap['pair']['token0Price']),
                        'token1Price': float(swap['pair']['token1Price']),
                        'dex': dex
                    }
                    trades.append(trade)
                    
            except Exception as e:
                logger.error(f"Error querying {dex}: {str(e)}", exc_info=True)
                continue
            
        return sorted(trades, key=lambda x: x['timestamp'])

def main():
    # Initialize analyzer with the configured API key
    analyzer = WalletHistoryAnalyzer()
    
    try:
        # Load and analyze transactions
        transactions = analyzer.load_transactions()
        wallet_data = analyzer.analyze_wallet(transactions)
        
        # Generate report
        analyzer.generate_report(wallet_data)
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main() 