import json
import requests
from pathlib import Path
from typing import Dict, Optional
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize price cache
price_cache: Dict[str, Optional[Dict]] = {}

def fetch_current_price(token_address: str, symbol: str, chain: str = None) -> Optional[Dict]:
    """Fetch current price and metadata for a token from DexScreener"""
    # Check cache first
    token_address = token_address.lower()
    cache_key = (token_address, chain)
    if cache_key in price_cache:
        return price_cache[cache_key]
    
    api_url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    dexscreener_url = f"https://dexscreener.com/{chain}/{token_address}" if chain else f"https://dexscreener.com/tokens/{token_address}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # Check if data and pairs exist and are not None
            exists_on_dexscreener = bool(data and 'pairs' in data and data['pairs'])
            
            if exists_on_dexscreener:
                print(f"\nAvailable pairs for {symbol}")
                print(f"Contract: {token_address}")
                print(f"DexScreener: {dexscreener_url}")
                print("-" * 80)
                # Get all valid pairs with price
                valid_pairs = []
                for pair in data['pairs']:
                    try:
                        # Print all pair info for debugging
                        price_usd = pair.get('priceUsd', 'N/A')
                        liquidity = pair.get('liquidity', {}).get('usd', 'N/A')
                        volume = pair.get('volume', {}).get('h24', 'N/A')
                        fdv = pair.get('fdv', 'N/A')
                        market_cap = pair.get('marketCap', 'N/A')
                        print(f"Chain: {pair.get('chainId', 'unknown')}")
                        print(f"DEX: {pair.get('dexId', 'unknown')}")
                        print(f"Price: ${price_usd}")
                        print(f"Liquidity: ${liquidity}")
                        print(f"24h Volume: ${volume}")
                        print(f"Market Cap: ${market_cap}")
                        print(f"FDV: ${fdv}")
                        print(f"Pair: {pair.get('baseToken', {}).get('symbol', symbol)} / {pair.get('quoteToken', {}).get('symbol', 'unknown')}")
                        print(f"Pair Address: {pair.get('pairAddress', 'unknown')}")
                        
                        # Add warning for low liquidity
                        try:
                            liq_float = float(liquidity) if liquidity != 'N/A' else 0
                            if liq_float < 1000:
                                print("⚠️ WARNING: This pair has very low liquidity (< $1,000)")
                        except (ValueError, TypeError):
                            pass
                            
                        print("-" * 40)
                        
                        # Basic validation - just need a valid price
                        try:
                            price_usd = float(price_usd) if price_usd != 'N/A' else 0
                            liquidity_usd = float(liquidity) if liquidity != 'N/A' else 0
                            volume_24h = float(volume) if volume != 'N/A' else 0
                            market_cap_usd = float(market_cap) if market_cap != 'N/A' else 0
                            fdv_usd = float(fdv) if fdv != 'N/A' else 0
                        except (ValueError, TypeError):
                            continue
                            
                        # Accept any pair with a price > 0, regardless of liquidity
                        if price_usd <= 0:
                            continue
                            
                        # If chain is specified, only accept pairs from that chain
                        if chain and pair.get('chainId', '').lower() != chain.lower():
                            continue
                        
                        # Calculate popularity score - still use this for sorting
                        popularity_score = liquidity_usd + (volume_24h * 2)
                        
                        valid_pairs.append({
                            'chain': pair.get('chainId'),
                            'dex': pair.get('dexId'),
                            'price_usd': price_usd,
                            'liquidity_usd': liquidity_usd,
                            'volume_24h': volume_24h,
                            'market_cap': market_cap_usd,
                            'fdv': fdv_usd,
                            'pair_address': pair.get('pairAddress'),
                            'quote_token': pair.get('quoteToken', {}).get('symbol'),
                            'popularity_score': popularity_score
                        })
                    except Exception as e:
                        print(f"Error processing pair: {str(e)}")
                        continue
                
                if valid_pairs:
                    # Sort by popularity score
                    valid_pairs.sort(key=lambda x: x['popularity_score'], reverse=True)
                    best_pair = valid_pairs[0]
                    
                    result = {
                        'name': symbol,
                        'symbol': symbol,
                        'current_price': best_pair['price_usd'],
                        'liquidity': best_pair['liquidity_usd'],
                        'volume_24h': best_pair['volume_24h'],
                        'market_cap': best_pair['market_cap'],
                        'fdv': best_pair['fdv'],
                        'chain': best_pair['chain'],
                        'dex': best_pair['dex'],
                        'quote_token': best_pair['quote_token'],
                        'pair_address': best_pair['pair_address'],
                        'contract_address': token_address,
                        'dexscreener_url': dexscreener_url,
                        'is_low_liquidity': best_pair['liquidity_usd'] < 1000,
                        'exists_on_dexscreener': exists_on_dexscreener,
                        'is_valid': True
                    }
                else:
                    # Token exists on DexScreener but has no valid pairs (potential rug)
                    result = {
                        'name': symbol,
                        'symbol': symbol,
                        'current_price': None,
                        'liquidity': 0,
                        'volume_24h': 0,
                        'market_cap': 0,
                        'fdv': 0,
                        'chain': chain,
                        'dex': None,
                        'quote_token': None,
                        'pair_address': None,
                        'contract_address': token_address,
                        'dexscreener_url': dexscreener_url,
                        'is_low_liquidity': True,
                        'exists_on_dexscreener': exists_on_dexscreener,
                        'is_valid': False
                    }
                    print(f"Token exists on DexScreener but has no valid pairs (potential rug)")
            else:
                # Token not found in DexScreener's database
                result = {
                    'name': symbol,
                    'symbol': symbol,
                    'current_price': None,
                    'liquidity': 0,
                    'volume_24h': 0,
                    'market_cap': 0,
                    'fdv': 0,
                    'chain': chain,
                    'dex': None,
                    'quote_token': None,
                    'pair_address': None,
                    'contract_address': token_address,
                    'dexscreener_url': dexscreener_url,
                    'is_low_liquidity': True,
                    'exists_on_dexscreener': False,
                    'is_valid': False
                }
                print(f"Token not found in DexScreener's database: {symbol} ({token_address})")
            
            price_cache[cache_key] = result
            return result
        else:
            # API error
            result = {
                'name': symbol,
                'symbol': symbol,
                'current_price': None,
                'liquidity': 0,
                'volume_24h': 0,
                'market_cap': 0,
                'fdv': 0,
                'chain': chain,
                'dex': None,
                'quote_token': None,
                'pair_address': None,
                'contract_address': token_address,
                'dexscreener_url': dexscreener_url,
                'is_low_liquidity': True,
                'exists_on_dexscreener': False,
                'is_valid': False
            }
            price_cache[cache_key] = result
            return result
            
    except Exception as e:
        print(f"Exception while fetching price for {symbol} ({token_address}): {str(e)}")
        return None

def main():
    # Get all JSON files in the testdata directory
    testdata_dir = Path(__file__).parent
    transaction_files = list(testdata_dir.glob('transactions_*.json'))
    
    # Track unique tokens with their chains
    unique_tokens = {}
    
    # Process transaction files
    print("\nProcessing transaction files...")
    for file_path in transaction_files:
        print(f"\nReading {file_path.name}...")
        try:
            with open(file_path, 'r') as f:
                tx_data = json.load(f)
            
            # Process each chain's transactions
            for chain, chain_txs in tx_data.get('transactions_by_chain', {}).items():
                for tx in chain_txs:
                    if 'transaction' in tx and 'token' in tx['transaction']:
                        token_info = tx['transaction']['token']
                        if 'contract' in token_info:
                            contract = token_info['contract'].lower()
                            if contract not in unique_tokens:
                                unique_tokens[contract] = {
                                    'name': token_info.get('name', ''),
                                    'symbol': token_info.get('symbol', ''),
                                    'decimals': token_info.get('decimals'),
                                    'chain': chain
                                }
                            
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
    
    # Fetch current prices
    print(f"\nFetching current prices for {len(unique_tokens)} tokens...")
    results = {}
    
    for address, data in unique_tokens.items():
        # Get current price and metadata
        price_data = fetch_current_price(address, data['symbol'], data['chain'])
        
        # Store results
        results[address] = {
            'name': data['name'],
            'symbol': data['symbol'],
            'decimals': data['decimals'],
            'chain': data['chain']
        }
        
        if price_data:
            results[address].update(price_data)
    
    # Save results
    print("\nSaving results...")
    output_file = testdata_dir / 'token_prices.json'
    
    formatted_results = {
        'metadata': {
            'timestamp': int(time.time()),
            'total_tokens': len(results)
        },
        'tokens': {
            address: {
                # Token metadata
                'name': data['name'],
                'symbol': data['symbol'],
                'decimals': data['decimals'],
                'chain': data['chain'],
                'contract_address': data.get('contract_address', address),
                
                # Price and liquidity data
                'current_price': data.get('current_price'),
                'liquidity': data.get('liquidity', 0),
                'volume_24h': data.get('volume_24h', 0),
                'market_cap': data.get('market_cap', 0),
                'fdv': data.get('fdv', 0),
                
                # Exchange data
                'dex': data.get('dex'),
                'quote_token': data.get('quote_token'),
                'pair_address': data.get('pair_address'),
                
                # Status flags
                'is_valid': data.get('is_valid', False),
                'is_low_liquidity': data.get('is_low_liquidity', True),
                'exists_on_dexscreener': data.get('exists_on_dexscreener', False),
                
                # Reference
                'dexscreener_url': f"https://dexscreener.com/{data['chain']}/{address}"
            }
            for address, data in results.items()
        }
    }
    
    with open(output_file, 'w') as f:
        json.dump(formatted_results, f, indent=2)
    
    print(f"\nToken prices saved to {output_file}")
    
    # Print summary
    print("\nPrice Summary:")
    for address, data in formatted_results['tokens'].items():
        print(f"\n{data['name']} ({data['symbol']}) on {data['chain']}:")
        if data['exists_on_dexscreener']:
            if data['is_valid']:
                print(f"  Current price: ${data['current_price']:.6f}" if data['current_price'] else "  Current price: N/A")
                print(f"  Liquidity: ${data['liquidity']:,.2f}" if data['liquidity'] else "  Liquidity: $0")
                print(f"  24h Volume: ${data['volume_24h']:,.2f}" if data['volume_24h'] else "  24h Volume: $0")
                print(f"  Market Cap: ${data['market_cap']:,.2f}" if data['market_cap'] else "  Market Cap: N/A")
                print(f"  FDV: ${data['fdv']:,.2f}" if data['fdv'] else "  FDV: N/A")
                print(f"  DEX: {data['dex']}")
                print(f"  Pair: {data['quote_token']}")
                if data['is_low_liquidity']:
                    print("  ⚠️ WARNING: Low liquidity")
            else:
                print("  ⚠️ Token exists but has no valid pairs (potential rug)")
        else:
            print("  ❌ Token not found on DexScreener")
        print(f"  Link: {data['dexscreener_url']}")

if __name__ == "__main__":
    main() 