import requests
from datetime import datetime
import re
import json
import time

class MultiChainTokenTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        # Define chain IDs for different networks
        self.endpoints = {
            'ethereum': {
                'url': 'https://api.etherscan.io/v2/api',
                'chain_id': 1
            },
            'base': {
                'url': 'https://api.etherscan.io/v2/api',  # Using v2 API for all chains
                'chain_id': 8453
            },
            'sonic': {
                'url': 'https://api.etherscan.io/v2/api',  # Using v2 API for all chains
                'chain_id': 146
            }
        }
        
    def get_transactions(self, address, chain='ethereum', start_block=0, end_block=99999999):
        chain_data = self.endpoints.get(chain.lower())
        if not chain_data:
            print(f"Unsupported chain: {chain}")
            return None
            
        params = {
            'chainid': chain_data['chain_id'],  # Add chainid parameter for v2 API
            'module': 'account',
            'action': 'tokentx',
            'address': address,
            'startblock': start_block,
            'endblock': end_block,
            'sort': 'desc',
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(chain_data['url'], params=params)
            data = response.json()
            
            if data['status'] == '1':
                return self._process_transactions(data['result'], address, chain)
            else:
                print(f"API Error for {chain}: {data.get('message', 'Unknown error')} - {data.get('result', '')}")
                return None
                
        except Exception as e:
            print(f"Error fetching {chain} transactions: {str(e)}")
            return None
            
    def _process_transactions(self, transactions, address, chain):
        trades = []
        for tx in transactions:
            try:
                # Convert timestamp to ISO format
                tx_time = datetime.fromtimestamp(int(tx['timeStamp'])).isoformat()
                
                # Calculate actual token amount
                amount = float(tx['value']) / (10 ** int(tx['tokenDecimal']))
                
                # Determine transaction type
                tx_type = 'buy' if tx['to'].lower() == address.lower() else 'sell'
                
                trade = {
                    'chain': chain,
                    'transaction': {
                        'hash': tx['hash'],
                        'timestamp': tx_time,
                        'block_number': int(tx['blockNumber']),
                        'type': tx_type,
                        'token': {
                            'name': tx['tokenName'],
                            'symbol': tx['tokenSymbol'],
                            'contract': tx['contractAddress'],
                            'decimals': int(tx['tokenDecimal'])
                        },
                        'amount': amount,
                        'from': tx['from'],
                        'to': tx['to'],
                        'gas_used': int(tx['gasUsed']),
                        'gas_price': int(tx['gasPrice'])
                    }
                }
                trades.append(trade)
            except Exception as e:
                print(f"Error processing transaction: {str(e)}")
                continue
                
        return trades

def is_valid_eth_address(address):
    pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
    return bool(pattern.match(address))

def save_to_json(data, address):
    filename = f"transactions_{address[:8]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    output = {
        'wallet_address': address,
        'timestamp': datetime.now().isoformat(),
        'total_transactions': sum(len(chain_data) for chain_data in data.values() if chain_data),
        'transactions_by_chain': data
    }
    
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    return filename

def main():
    API_KEY = "MDI1N6W7ZPKSKGEPIYUGT4RN4YFYRRE1QV"
    tracker = MultiChainTokenTracker(API_KEY)
    
    while True:
        address = input("Enter an Ethereum wallet address (or 'quit' to exit): ").strip()
        
        if address.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not is_valid_eth_address(address):
            print("Invalid Ethereum address. It should start with '0x' and be 42 characters long.")
            continue
            
        print("\nFetching transactions across all chains...")
        all_transactions = {}
        
        # Fetch transactions from all chains
        for chain in tracker.endpoints.keys():
            print(f"Fetching {chain} transactions...")
            transactions = tracker.get_transactions(address, chain)
            if transactions:
                all_transactions[chain] = transactions
            time.sleep(1)  # Respect rate limits
        
        if any(all_transactions.values()):
            # Save to JSON file
            filename = save_to_json(all_transactions, address)
            print(f"\nTransactions saved to {filename}")
            
            # Print summary
            print("\nTransaction Summary:")
            for chain, transactions in all_transactions.items():
                if transactions:
                    print(f"{chain.title()}: {len(transactions)} transactions")
                    
                    # Show sample of transactions
                    print("\nSample transactions:")
                    for tx in transactions[:3]:  # Show first 3 transactions
                        print(f"""
{chain.title()} Transaction:
    Time: {tx['transaction']['timestamp']}
    Type: {tx['transaction']['type'].upper()}
    Token: {tx['transaction']['token']['name']} ({tx['transaction']['token']['symbol']})
    Amount: {tx['transaction']['amount']:,.8f}
    Hash: {tx['transaction']['hash']}
                        """)
        else:
            print("No transactions found across any chain.")
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    print("Welcome to the Multi-Chain Token Transaction Tracker!")
    print("This tool tracks transactions across Ethereum, Base, and Sonic networks.")
    print("Type 'quit' at any time to exit.\n")
    main() 