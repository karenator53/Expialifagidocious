import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import time
from collections import defaultdict

class WalletAnalyzer:
    def __init__(self):
        self.testdata_dir = Path(__file__).parent
        self.current_prices = self.load_current_prices()
        self.historical_prices = self.load_historical_prices()
        self.transactions = self.load_transactions()
        self.wallets = self.extract_wallets()
        
    def load_current_prices(self) -> Dict:
        """Load current token prices from token_prices.json"""
        file_path = self.testdata_dir / 'token_prices.json'
        if not file_path.exists():
            raise FileNotFoundError(f"Could not find token_prices.json in {self.testdata_dir}")
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data['tokens']
    
    def load_historical_prices(self) -> Dict:
        """Load historical token prices from historical_prices.json"""
        file_path = self.testdata_dir / 'historical_prices.json'
        if not file_path.exists():
            raise FileNotFoundError(f"Could not find historical_prices.json in {self.testdata_dir}")
            
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def load_transactions(self) -> List[Dict]:
        """Load all transaction files from the testdata directory"""
        transactions = []
        transaction_files = list(self.testdata_dir.glob('transactions_*.json'))
        
        if not transaction_files:
            raise FileNotFoundError(f"No transaction files found in {self.testdata_dir}")
            
        print("\nLoading transaction files:")
        for file_path in transaction_files:
            print(f"\nProcessing {file_path.name}...")
            with open(file_path, 'r') as f:
                tx_data = json.load(f)
                print(f"Found chains: {list(tx_data.get('transactions_by_chain', {}).keys())}")
                for chain, chain_txs in tx_data.get('transactions_by_chain', {}).items():
                    print(f"Chain {chain}: {len(chain_txs)} transactions")
                    if chain_txs:
                        print(f"Sample transaction structure:")
                        print(json.dumps(chain_txs[0], indent=2))
                transactions.append(tx_data)
        return transactions
    
    def extract_wallets(self) -> Dict[str, Dict]:
        """Extract all wallets and initialize their metrics"""
        wallets = {}
        print("\nExtracting wallet addresses:")
        for tx_file in self.transactions:
            for chain, chain_txs in tx_file.get('transactions_by_chain', {}).items():
                print(f"\nProcessing chain: {chain}")
                for tx in chain_txs:
                    if 'transaction' not in tx:
                        continue
                        
                    tx_data = tx['transaction']
                    if 'type' not in tx_data or 'from' not in tx_data or 'to' not in tx_data:
                        continue
                    
                    # For buys, the wallet is the 'to' address
                    # For sells, the wallet is the 'from' address
                    wallet = tx_data['to'].lower() if tx_data['type'] == 'buy' else tx_data['from'].lower()
                    
                    if wallet not in wallets:
                        print(f"Found wallet: {wallet} ({tx_data['type']})")
                        wallets[wallet] = {
                            'address': wallet,
                            'total_invested': 0.0,
                            'current_portfolio_value': 0.0,
                            'realized_pnl': 0.0,
                            'unrealized_pnl': 0.0,
                            'total_trades': 0,
                            'successful_trades': 0,
                            'rug_trades': 0,
                            'rug_losses': 0.0,
                            'tokens': {},
                            'holdings': defaultdict(float),
                            'buy_prices': defaultdict(list),
                            'trades': defaultdict(list)
                        }
        
        print(f"\nFound {len(wallets)} unique wallets")
        return wallets
    
    def analyze_transactions(self):
        """Analyze all transactions for all wallets"""
        for tx_file in self.transactions:
            for chain, chain_txs in tx_file.get('transactions_by_chain', {}).items():
                for tx in chain_txs:
                    if 'transaction' not in tx:
                        continue
                        
                    tx_data = tx['transaction']
                    if 'type' not in tx_data or 'from' not in tx_data or 'to' not in tx_data:
                        continue
                    
                    tx_type = tx_data['type']
                    wallet_address = tx_data['to'].lower() if tx_type == 'buy' else tx_data['from'].lower()
                    
                    if wallet_address not in self.wallets:
                        continue
                    
                    wallet = self.wallets[wallet_address]
                    token_info = tx_data['token']
                    token_address = token_info['contract'].lower()
                    amount = float(tx_data['amount'])
                    timestamp = tx_data['timestamp']
                    
                    # Get token current price info
                    token_data = self.current_prices.get(token_address, {})
                    current_price_raw = token_data.get('current_price')
                    current_price = float(current_price_raw) if current_price_raw is not None else 0.0
                    is_rug = token_data.get('is_low_liquidity', True) or not token_data.get('is_valid', False)
                    
                    # Get historical price at transaction time
                    historical_price_raw = self.historical_prices.get(token_address, {}).get('price_at_block')
                    historical_price = float(historical_price_raw) if historical_price_raw is not None else 0.0
                    
                    # Skip invalid transactions
                    if amount <= 0 or (historical_price == 0.0 and tx_type == 'sell'):
                        continue
                    
                    trade = {
                        'timestamp': timestamp,
                        'type': tx_type,
                        'amount': amount,
                        'price': historical_price,
                        'value': amount * historical_price,
                        'token_symbol': token_info['symbol'],
                        'token_name': token_info['name'],
                        'chain': chain
                    }
                    
                    # Initialize token data if not exists
                    if token_address not in wallet['tokens']:
                        wallet['tokens'][token_address] = {
                            'symbol': token_info['symbol'],
                            'name': token_info['name'],
                            'chain': chain,
                            'current_price': current_price,
                            'current_holdings': 0,
                            'total_bought': 0,
                            'total_sold': 0,
                            'realized_pnl': 0,
                            'unrealized_pnl': 0,
                            'is_rug': is_rug,
                            'trades': []
                        }
                    
                    # Update wallet metrics
                    wallet['total_trades'] += 1
                    wallet['trades'][token_address].append(trade)
                    
                    # Update holdings and calculate PnL
                    if tx_type == 'buy':
                        wallet['holdings'][token_address] += amount
                        wallet['buy_prices'][token_address].append((amount, historical_price))
                        wallet['total_invested'] += amount * historical_price
                        wallet['tokens'][token_address]['total_bought'] += amount
                    else:  # sell
                        wallet['holdings'][token_address] -= amount
                        wallet['tokens'][token_address]['total_sold'] += amount
                        
                        # Calculate realized PnL
                        if wallet['buy_prices'][token_address]:
                            cost_basis = self.calculate_cost_basis(amount, wallet['buy_prices'][token_address])
                            realized_pnl = (historical_price - cost_basis) * amount
                            wallet['realized_pnl'] += realized_pnl
                            wallet['tokens'][token_address]['realized_pnl'] += realized_pnl
                            
                            if realized_pnl > 0:
                                wallet['successful_trades'] += 1
                            if is_rug:
                                wallet['rug_trades'] += 1
                                wallet['rug_losses'] += abs(realized_pnl) if realized_pnl < 0 else 0
        
        # Calculate final positions and unrealized PnL for each wallet
        for wallet in self.wallets.values():
            for token_address, amount in wallet['holdings'].items():
                if amount > 0:
                    token_metrics = wallet['tokens'][token_address]
                    token_data = self.current_prices.get(token_address, {})
                    current_price_raw = token_data.get('current_price')
                    current_price = float(current_price_raw) if current_price_raw is not None else 0.0
                    
                    # Calculate cost basis for remaining tokens
                    if wallet['buy_prices'][token_address]:
                        avg_cost = sum(price * amt for amt, price in wallet['buy_prices'][token_address]) / sum(amt for amt, _ in wallet['buy_prices'][token_address])
                        unrealized_pnl = (current_price - avg_cost) * amount
                        token_metrics['unrealized_pnl'] = unrealized_pnl
                        wallet['unrealized_pnl'] += unrealized_pnl
                    
                    current_value = amount * current_price
                    token_metrics['current_holdings'] = amount
                    token_metrics['current_price'] = current_price
                    wallet['current_portfolio_value'] += current_value
    
    def generate_reports(self):
        """Generate reports for all wallets"""
        self.analyze_transactions()
        
        for wallet_address, wallet in self.wallets.items():
            print(f"\n{'='*80}")
            print(f"Wallet Analysis: {wallet_address}")
            print(f"{'='*80}")
            
            print("\nPortfolio Summary:")
            print(f"Total Invested: ${wallet['total_invested']:.2f}")
            print(f"Current Portfolio Value: ${wallet['current_portfolio_value']:.2f}")
            print(f"Realized PnL: ${wallet['realized_pnl']:.2f}")
            print(f"Unrealized PnL: ${wallet['unrealized_pnl']:.2f}")
            print(f"Total PnL: ${(wallet['realized_pnl'] + wallet['unrealized_pnl']):.2f}")
            
            if wallet['total_trades'] > 0:
                success_rate = (wallet['successful_trades'] / wallet['total_trades']) * 100
                print(f"\nTrade Statistics:")
                print(f"Total Trades: {wallet['total_trades']}")
                print(f"Successful Trades: {wallet['successful_trades']} ({success_rate:.1f}%)")
                print(f"Rug Pulls Encountered: {wallet['rug_trades']}")
                print(f"Losses from Rugs: ${wallet['rug_losses']:.2f}")
            
            print("\nCurrent Holdings:")
            for token_address, token_data in wallet['tokens'].items():
                if token_data['current_holdings'] > 0:
                    print(f"\n{token_data['symbol']} ({token_data['name']}):")
                    print(f"  Chain: {token_data['chain']}")
                    print(f"  Holdings: {token_data['current_holdings']:.4f}")
                    print(f"  Current Price: ${token_data['current_price']:.6f}")
                    print(f"  Current Value: ${token_data['current_holdings'] * token_data['current_price']:.2f}")
                    print(f"  Realized PnL: ${token_data['realized_pnl']:.2f}")
                    print(f"  Unrealized PnL: ${token_data['unrealized_pnl']:.2f}")
                    if token_data['is_rug']:
                        print("  WARNING: Possible rug pull (low liquidity or invalid token)")

def main():
    analyzer = WalletAnalyzer()
    analyzer.generate_reports()

if __name__ == "__main__":
    main() 