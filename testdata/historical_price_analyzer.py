import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from tqdm import tqdm
import logging
from datetime import datetime
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor
import asyncio
from functools import partial

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# DRPC endpoints
DRPC_ENDPOINTS = {
    'ethereum': 'https://lb.drpc.org/ogrpc?network=ethereum&dkey=At-n0kIQ5kxdp0Dgm1C_C8fog4Lf1RYR74rJKuk0h5Qw',
    'base': 'https://lb.drpc.org/ogrpc?network=base&dkey=At-n0kIQ5kxdp0Dgm1C_C8fog4Lf1RYR74rJKuk0h5Qw',
    'sonic': 'https://lb.drpc.org/ogrpc?network=sonic&dkey=At-n0kIQ5kxdp0Dgm1C_C8fog4Lf1RYR74rJKuk0h5Qw'
}

# Chain-specific configurations
CHAIN_IDS = {
    'ethereum': 1,
    'base': 8453,
    'sonic': 146
}

# Initialize Web3 instances with chain verification
w3_instances = {}
for chain, url in DRPC_ENDPOINTS.items():
    try:
        w3 = Web3(Web3.HTTPProvider(url))
        
        # Verify chain ID
        chain_id = w3.eth.chain_id
        expected_id = CHAIN_IDS.get(chain)
        if chain_id != expected_id:
            logging.error(f"Chain ID mismatch for {chain}. Expected {expected_id}, got {chain_id}")
            continue
        
        # Check if node is synced
        if w3.eth.syncing:
            logging.warning(f"Node for {chain} is still syncing")
        
        w3_instances[chain] = w3
        logging.info(f"Successfully initialized {chain} connection")
    except Exception as e:
        logging.error(f"Failed to initialize {chain}: {str(e)}")

# Cache for block numbers and prices
block_cache = {}
price_cache = {}

# Chain-specific token addresses
CHAIN_TOKENS = {
    'ethereum': {
        'USDC': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
        'WETH': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    },
    'base': {
        'USDC': '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913',
        'WETH': '0x4200000000000000000000000000000000000006'
    },
    'sonic': {
        'USDC': '0x1C7a460413dD4e964f96D8dFC56E7223cE88CD85',  # Sonic USDC
        'WETH': '0x5300000000000000000000000000000000000004'   # Sonic WETH
    }
}

# Chain-specific DEX factory addresses
FACTORY_ADDRESSES = {
    'ethereum': [
        '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f',  # Uniswap V2
        '0x1F98431c8aD98523631AE4a59f267346ea31F984'   # Uniswap V3
    ],
    'base': [
        '0x8909dc15e40173ff4699343b6eb8132c65e18ec6',  # BaseSwap
        '0x2E1750E203A97814e550B9A91Dc35660d72EF1D3'   # Uniswap V3
    ],
    'sonic': [
        '0x9B3336186a38E1b6c21955d112dbb0343Ee061eE',  # SonicSwap
        '0x7C17611Ed67D562D1F00ce82eebD39Cb7B595472',  # AlienBase
        '0x4fe80C33b27fB41946766C00e7A1F35A0D9E5ce3'   # SonicDex
    ]
}

# Chain-specific WETH addresses
WETH_ADDRESSES = {
    'ethereum': Web3.to_checksum_address("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),
    'base': Web3.to_checksum_address("0x4200000000000000000000000000000000000006"),
    'sonic': Web3.to_checksum_address("0x5300000000000000000000000000000000000004")
}

# Factory ABI for pair lookup
FACTORY_ABI = [
    {
        "constant": True,
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"}
        ],
        "name": "getPair",
        "outputs": [{"internalType": "address", "name": "pair", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Event signatures
SWAP_EVENT_V2 = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
SWAP_EVENT_V3 = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"

# Add ERC20 ABI for decimals lookup
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Add V3 Pool ABI for slot0 lookup
V3_POOL_ABI = [
    {
        "inputs": [],
        "name": "slot0",
        "outputs": [
            {"name": "sqrtPriceX96", "type": "uint160"},
            {"name": "tick", "type": "int24"},
            {"name": "observationIndex", "type": "uint16"},
            {"name": "observationCardinality", "type": "uint16"},
            {"name": "observationCardinalityNext", "type": "uint16"},
            {"name": "feeProtocol", "type": "uint8"},
            {"name": "unlocked", "type": "bool"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Cache for decimals and ETH prices
decimals_cache = {}
eth_price_cache = {}

def load_current_prices() -> Dict:
    """Load current prices from token_prices.json"""
    try:
        # Try multiple locations
        possible_paths = [
            Path('token_prices.json'),
            Path('testdata/token_prices.json'),
            Path(__file__).parent / 'token_prices.json',
            Path.cwd() / 'token_prices.json'
        ]
        
        for path in possible_paths:
            if path.exists():
                print(f"Loading prices from {path.absolute()}")
                with open(path, 'r') as f:
                    return json.load(f)
        
        print("Warning: Could not find token_prices.json in any expected location")
        return {'tokens': {}}
    except Exception as e:
        logging.error(f"Error loading token_prices.json: {str(e)}")
        return {'tokens': {}}

def load_transactions() -> List[Dict]:
    """Load all transaction files and combine them"""
    transactions = []
    
    # Try multiple locations for transaction files
    possible_dirs = [
        Path('.'),
        Path('testdata'),
        Path(__file__).parent,
        Path.cwd()
    ]
    
    print("\nSearching for transaction files...")
    for directory in possible_dirs:
        if not directory.exists():
            continue
            
        print(f"Looking in: {directory.absolute()}")
        transaction_files = list(directory.glob('transactions_*.json'))
        
        if transaction_files:
            print(f"Found {len(transaction_files)} transaction files")
            for file_path in transaction_files:
                try:
                    print(f"\nProcessing {file_path.name}...")
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        if 'transactions_by_chain' not in data:
                            print(f"Warning: No transactions_by_chain in {file_path.name}")
                            continue
                            
                        for chain, chain_txs in data['transactions_by_chain'].items():
                            if not isinstance(chain_txs, list):
                                print(f"Warning: Invalid transactions format for chain {chain} in {file_path.name}")
                                continue
                                
                            print(f"  Found {len(chain_txs)} transactions for chain {chain}")
                            for tx in chain_txs:
                                if not isinstance(tx, dict):
                                    print(f"Warning: Invalid transaction format in {chain}")
                                    continue
                                tx['chain'] = chain
                                transactions.append(tx)
                except json.JSONDecodeError as e:
                    logging.error(f"JSON decode error in {file_path}: {str(e)}")
                except Exception as e:
                    logging.error(f"Error loading {file_path}: {str(e)}")
            
            # If we found files in this directory, stop searching
            if transactions:
                break
    
    print(f"\nTotal transactions loaded: {len(transactions)}")
    if not transactions:
        print("\nNo transactions found. Please ensure transaction files are in the correct format:")
        print("Expected format: transactions_*.json with structure:")
        print("""
        {
            "transactions_by_chain": {
                "ethereum": [...],
                "base": [...],
                "sonic": [...]
            }
        }
        """)
        print("\nLooked in the following locations:")
        for directory in possible_dirs:
            print(f"- {directory.absolute()}")
    
    return transactions

def get_block_by_timestamp(timestamp: str, chain: str) -> Optional[int]:
    """Get the closest block number for a given timestamp with optimized binary search"""
    cache_key = (timestamp, chain)
    if cache_key in block_cache:
        return block_cache[cache_key]
    
    try:
        # Parse timestamp
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            timestamp_int = int(dt.timestamp())
        except Exception as e:
            print(f"Error parsing timestamp {timestamp}: {str(e)}")
            return None
        
        w3 = w3_instances.get(chain)
        if not w3:
            print(f"No web3 instance for chain {chain}")
            return None
        
        # Get latest block for upper bound
        try:
            latest_block = w3.eth.get_block('latest')
            if not latest_block:
                print(f"Could not get latest block for chain {chain}")
                return None
                
            latest_number = latest_block.number
            latest_timestamp = latest_block.timestamp
            
            # If target timestamp is after latest block, use latest block
            if timestamp_int >= latest_timestamp:
                block_cache[cache_key] = latest_number
                return latest_number
                
            # If target timestamp is too old (more than ~1 year), estimate block
            if latest_timestamp - timestamp_int > 31536000:  # ~1 year in seconds
                # Estimate using average block time (13s for ETH, adjust for other chains)
                block_time = 13 if chain == 'ethereum' else 2  # 2s for faster chains
                estimated_block = latest_number - ((latest_timestamp - timestamp_int) // block_time)
                print(f"Target timestamp is old, using estimated block {estimated_block}")
                block_cache[cache_key] = estimated_block
                return estimated_block
                
        except Exception as e:
            print(f"Error getting latest block for chain {chain}: {str(e)}")
            return None
        
        # Binary search for block
        left = 1
        right = latest_number
        closest_block = None
        closest_diff = float('inf')
        
        print(f"Searching for block with timestamp {timestamp_int} between blocks 1 and {latest_number}")
        
        while left <= right:
            mid = (left + right) // 2
            try:
                block = w3.eth.get_block(mid)
                if not block:
                    print(f"Could not get block {mid}")
                    break
                    
                block_timestamp = block.timestamp
                diff = abs(block_timestamp - timestamp_int)
                
                if diff < closest_diff:
                    closest_block = mid
                    closest_diff = diff
                
                if block_timestamp == timestamp_int:
                    block_cache[cache_key] = mid
                    return mid
                elif block_timestamp < timestamp_int:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            except Exception as e:
                print(f"Error getting block {mid}: {str(e)}")
                break
        
        if closest_block is not None:
            print(f"Found closest block {closest_block} with timestamp difference of {closest_diff} seconds")
            block_cache[cache_key] = closest_block
            return closest_block
            
        print(f"Could not find block for timestamp {timestamp}")
        return None
            
    except Exception as e:
        print(f"Error getting block for timestamp {timestamp}: {str(e)}")
        return None

def get_pair_address(token_address: str, chain: str) -> Optional[str]:
    """Get the pair address for a token/WETH pair with improved error handling"""
    weth_address = WETH_ADDRESSES.get(chain)
    if not weth_address:
        print(f"No WETH address found for chain {chain}")
        return None
    
    w3 = w3_instances.get(chain)
    if not w3:
        print(f"No web3 instance for chain {chain}")
        return None
    
    # Convert token address to checksum format
    try:
        token_address = Web3.to_checksum_address(token_address)
    except Exception as e:
        print(f"Invalid token address format for {token_address}: {str(e)}")
        return None
    
    # Try each factory
    factories = FACTORY_ADDRESSES.get(chain, [])
    if not factories:
        print(f"No factory addresses found for chain {chain}")
        return None
        
    print(f"Checking {len(factories)} factories for {token_address} on chain {chain}")
    
    for factory_address in factories:
        try:
            # First verify the factory contract exists
            code = w3.eth.get_code(factory_address)
            if not code:
                print(f"No code found at factory address {factory_address}")
                continue
            
            # Try direct eth_call first (faster)
            pair = eth_call(
                factory_address,
                f"0xe6a43905{token_address[2:].lower().zfill(64)}{weth_address[2:].lower().zfill(64)}",
                'latest',
                chain
            )
            
            if pair and pair != "0x0000000000000000000000000000000000000000000000000000000000000000":
                try:
                    pair_address = Web3.to_checksum_address("0x" + pair[-40:])
                    # Verify pair contract exists
                    if w3.eth.get_code(pair_address):
                        print(f"Found valid pair {pair_address} at factory {factory_address}")
                        return pair_address
                    else:
                        print(f"No code found at pair address {pair_address}")
                except Exception as e:
                    print(f"Error validating pair address: {str(e)}")
                    continue
            else:
                print(f"No pair found at factory {factory_address}")
            
        except Exception as e:
            print(f"Error checking factory {factory_address}: {str(e)}")
            continue
    
    print(f"No valid trading pair found for {token_address} on chain {chain} after checking all factories")
    return None

def get_token_decimals(token_address: str) -> Optional[int]:
    """Get token decimals from contract"""
    if token_address in decimals_cache:
        return decimals_cache[token_address]
    
    try:
        # Convert to checksum address
        try:
            token_address = Web3.to_checksum_address(token_address)
        except Exception as e:
            print(f"Invalid token address format for {token_address}: {str(e)}")
            return None
        
        # First try eth_call directly (faster)
        try:
            decimals_data = eth_call(
                token_address,
                "0x313ce567",  # decimals()
                'latest',
                'ethereum'  # Use Ethereum as default chain for decimals
            )
            if decimals_data:
                decimals = int(decimals_data[2:], 16)
                if 0 <= decimals <= 77:  # Sanity check for reasonable decimals range
                    decimals_cache[token_address] = decimals
                    return decimals
                else:
                    print(f"Invalid decimals {decimals} for token {token_address}")
        except Exception as e:
            print(f"Error getting decimals via eth_call for {token_address}: {str(e)}")
        
        # Fallback to contract method
        try:
            token_contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
            decimals = token_contract.functions.decimals().call()
            if 0 <= decimals <= 77:  # Sanity check for reasonable decimals range
                decimals_cache[token_address] = decimals
                return decimals
            else:
                print(f"Invalid decimals {decimals} for token {token_address}")
        except Exception as e:
            print(f"Error getting decimals via contract for {token_address}: {str(e)}")
        
        # If both methods fail, default to 18
        print(f"Could not get decimals for {token_address}, defaulting to 18")
        decimals_cache[token_address] = 18
        return 18
        
    except Exception as e:
        print(f"Error getting decimals for {token_address}: {str(e)}")
        return None

def get_eth_price_at_block(block_number: int, chain: str) -> Optional[float]:
    """Get ETH price in USD at a specific block"""
    if block_number in eth_price_cache:
        return eth_price_cache[block_number]
    
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            print(f"No web3 instance for chain {chain}")
            return None
        
        # Get chain-specific USDC/WETH addresses
        usdc_address = CHAIN_TOKENS[chain]['USDC']
        weth_address = CHAIN_TOKENS[chain]['WETH']
        
        if not usdc_address or not weth_address:
            print(f"Missing token addresses for chain {chain}")
            return None
            
        usdc_decimals = 6  # USDC always has 6 decimals
        
        # Get pair address
        pair_address = get_pair_address(usdc_address, chain)
        if not pair_address:
            print(f"No USDC/WETH pair found for chain {chain}")
            return None
        
        print(f"Found USDC/WETH pair {pair_address} for chain {chain}")
        
        # Get swap events
        try:
            logs = w3.eth.get_logs({
                'fromBlock': block_number - 5,
                'toBlock': block_number,
                'topics': [SWAP_EVENT_V2],
                'address': pair_address
            })
            
            if not logs:
                print(f"No swap events found for USDC/WETH pair at block {block_number}")
                return None
                
            print(f"Found {len(logs)} swap events for USDC/WETH pair")
            
            # Use the most recent swap
            event = logs[-1]
            data = event['data'][2:]
            amount0 = int(data[:64], 16)
            amount1 = int(data[64:128], 16)
            
            if amount0 == 0 or amount1 == 0:
                print(f"Invalid amounts in swap event: amount0={amount0}, amount1={amount1}")
                return None
            
            # Calculate ETH price in USD
            eth_decimals = 18
            eth_amount = amount0 / (10 ** eth_decimals)
            usdc_amount = amount1 / (10 ** usdc_decimals)
            eth_price = usdc_amount / eth_amount
            
            print(f"Calculated ETH price at block {block_number}: ${eth_price:,.2f}")
            
            eth_price_cache[block_number] = eth_price
            return eth_price
            
        except Exception as e:
            print(f"Error getting swap events for USDC/WETH pair: {str(e)}")
            return None
            
    except Exception as e:
        print(f"Error getting ETH price at block {block_number}: {str(e)}")
        return None

def calculate_v3_price(sqrt_price_x96: int, token0_decimals: int, token1_decimals: int) -> Optional[float]:
    """Calculate price from V3 sqrtPriceX96"""
    try:
        if sqrt_price_x96 <= 0:
            print(f"Invalid sqrtPriceX96: {sqrt_price_x96}")
            return None
            
        if token0_decimals < 0 or token1_decimals < 0:
            print(f"Invalid decimals: token0_decimals={token0_decimals}, token1_decimals={token1_decimals}")
            return None
        
        # Convert sqrtPriceX96 to price
        try:
            price = (sqrt_price_x96 / (2 ** 96)) ** 2
        except Exception as e:
            print(f"Error calculating price from sqrtPriceX96: {str(e)}")
            return None
        
        # Adjust for decimals
        try:
            decimal_adjustment = 10 ** (token1_decimals - token0_decimals)
            final_price = price * decimal_adjustment
            
            if not (0 < final_price < 1e20):  # Sanity check for reasonable price range
                print(f"Calculated price {final_price} is outside reasonable range")
                return None
                
            print(f"Calculated V3 price: {final_price}")
            return final_price
            
        except Exception as e:
            print(f"Error adjusting price for decimals: {str(e)}")
            return None
            
    except Exception as e:
        print(f"Error calculating V3 price: {str(e)}")
        return None

def verify_contract(address: str, chain: str) -> bool:
    """Verify if an address is a contract and has code"""
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            print(f"No web3 instance for chain {chain}")
            return False
        
        # Convert to checksum address
        try:
            address = Web3.to_checksum_address(address)
        except Exception as e:
            print(f"Invalid address format for {address}: {str(e)}")
            return False
        
        # Check if address exists
        try:
            code = w3.eth.get_code(address)
            has_code = len(code) > 0
            if not has_code:
                print(f"No contract code found at {address} on chain {chain}")
            return has_code
        except Exception as e:
            print(f"Error getting code for {address} on chain {chain}: {str(e)}")
            return False
            
    except Exception as e:
        print(f"Error verifying contract {address}: {str(e)}")
        return False

def get_block_with_validation(block_number: int, chain: str) -> Optional[Dict]:
    """Get block data with comprehensive validation"""
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            print(f"No web3 instance for chain {chain}")
            return None
        
        # First try getting block by number with full transactions
        try:
            block = w3.eth.get_block(block_number, full_transactions=True)
            if not block:
                print(f"Block {block_number} not found on chain {chain}")
                return None
        except Exception as e:
            print(f"Failed to get block {block_number} with full transactions: {str(e)}")
            return None
        
        # Verify block has expected fields
        required_fields = ['number', 'timestamp', 'transactions', 'hash']
        missing_fields = [field for field in required_fields if not hasattr(block, field)]
        if missing_fields:
            print(f"Block {block_number} missing required fields: {', '.join(missing_fields)}")
            return None
        
        # Get transaction count through dedicated endpoint for verification
        try:
            tx_count = w3.eth.get_block_transaction_count(block_number)
            if tx_count != len(block.transactions):
                print(f"Transaction count mismatch for block {block_number}: expected {tx_count}, got {len(block.transactions)}")
        except Exception as e:
            print(f"Failed to verify transaction count for block {block_number}: {str(e)}")
        
        # Check for uncle blocks
        try:
            uncle_count = w3.eth.get_uncle_count(block_number)
            if uncle_count > 0:
                print(f"Block {block_number} has {uncle_count} uncles")
                
                # Get surrounding blocks
                try:
                    prev_block = w3.eth.get_block(block_number - 1, full_transactions=True)
                    next_block = w3.eth.get_block(block_number + 1, full_transactions=True)
                    
                    # Compare timestamps to ensure sequence
                    if not (prev_block.timestamp <= block.timestamp <= next_block.timestamp):
                        print(f"Block {block_number} has inconsistent timestamp sequence")
                        print(f"Previous block timestamp: {prev_block.timestamp}")
                        print(f"Current block timestamp: {block.timestamp}")
                        print(f"Next block timestamp: {next_block.timestamp}")
                    
                    # Use block with most transactions and consistent timestamp
                    blocks = [(b, len(b.transactions)) for b in [block, prev_block, next_block] 
                             if prev_block.timestamp <= b.timestamp <= next_block.timestamp]
                    if blocks:
                        block = max(blocks, key=lambda x: x[1])[0]
                        print(f"Selected block {block.number} with {len(block.transactions)} transactions")
                except Exception as e:
                    print(f"Error checking surrounding blocks: {str(e)}")
        except Exception as e:
            print(f"Failed to check uncles for block {block_number}: {str(e)}")
        
        return block
    except Exception as e:
        print(f"Error getting block {block_number} on chain {chain}: {str(e)}")
        return None

def validate_timestamp_with_gas(block_number: int, chain: str, timestamp: int) -> bool:
    """Validate timestamp using gas price data"""
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            return False
        
        # Get gas prices from surrounding blocks
        current_gas = w3.eth.gas_price
        block_gas = w3.eth.get_block(block_number).base_fee_per_gas
        
        # Get max priority fee
        max_priority_fee = w3.eth.max_priority_fee_per_gas
        
        # Calculate expected total gas
        expected_total = block_gas + max_priority_fee
        
        # If gas prices are significantly different, timestamp might be wrong
        if abs(current_gas - expected_total) / current_gas > 0.5:  # 50% difference threshold
            logging.warning(f"Gas price discrepancy at block {block_number}, timestamp may be incorrect")
            return False
        
        return True
    except Exception as e:
        logging.debug(f"Error validating timestamp with gas: {str(e)}")
        return True  # Default to True if validation fails

def get_token_storage_data(token_address: str, chain: str) -> Dict:
    """Get additional token data from contract storage"""
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            return {}
        
        # Common storage slots for ERC20 tokens
        total_supply_slot = 0x2
        name_slot = 0x3
        symbol_slot = 0x4
        
        data = {
            'total_supply': w3.eth.get_storage_at(token_address, total_supply_slot),
            'name_raw': w3.eth.get_storage_at(token_address, name_slot),
            'symbol_raw': w3.eth.get_storage_at(token_address, symbol_slot)
        }
        
        return data
    except Exception as e:
        logging.debug(f"Error getting token storage data: {str(e)}")
        return {}

def get_historical_price(token_address: str, block_number: int, chain: str) -> Optional[float]:
    """Get historical price with comprehensive validation and fallbacks"""
    cache_key = (token_address, block_number, chain)
    if cache_key in price_cache:
        return price_cache[cache_key]
    
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            print(f"No web3 instance for chain {chain}")
            return None
        
        # Verify contract exists and has code
        if not verify_contract(token_address, chain):
            print(f"Contract {token_address} does not exist or has no code on chain {chain}")
            return None
        
        # Get validated block data
        block = get_block_with_validation(block_number, chain)
        if not block:
            print(f"Could not validate block {block_number} on chain {chain}")
            return None
        
        # Get ETH price first since we'll need it for all methods
        eth_price = get_eth_price_at_block(block_number, chain)
        if not eth_price:
            print(f"Could not get ETH price at block {block_number}")
            return None
            
        print(f"Got ETH price ${eth_price:,.2f} at block {block_number}")
        
        # Try multiple price sources in order of reliability
        price = None
        
        # 1. Try V3 pool slot0 (most accurate)
        try:
            pair_address = get_pair_address(token_address, chain)
            if pair_address:
                print(f"Found V3 pair {pair_address} for {token_address} on {chain}")
                slot0_data = eth_call(
                    pair_address,
                    "0x3850c7bd", # slot0()
                    block_number,
                    chain
                )
                if slot0_data:
                    sqrt_price_x96 = int(slot0_data[:66], 16)
                    raw_price = calculate_v3_price(
                        sqrt_price_x96,
                        get_token_decimals(token_address),
                        get_token_decimals(WETH_ADDRESSES[chain])
                    )
                    if raw_price:
                        price = raw_price * eth_price
                        print(f"Got V3 price for {token_address} at block {block_number}: ${price:,.6f} USD")
                    else:
                        print(f"Could not calculate V3 price from sqrt_price_x96")
                else:
                    print(f"No slot0 data for pair {pair_address}")
            else:
                print(f"No V3 pair found for {token_address} on {chain}")
        except Exception as e:
            print(f"V3 price lookup failed: {str(e)}")
        
        # 2. Try V2 swap events
        if not price:
            try:
                events = []
                # Use smaller ranges and pagination for better reliability
                for offset in range(0, 10, 2):
                    logs = w3.eth.get_logs({
                        'fromBlock': max(1, block_number - offset),
                        'toBlock': min(block_number + offset, w3.eth.block_number),
                        'topics': [SWAP_EVENT_V2],
                        'address': pair_address
                    })
                    if logs:
                        print(f"Found {len(logs)} V2 swap events for {token_address}")
                        events.extend([(log, None) for log in logs])
                        break
                
                if events:
                    raw_price = process_swap_events(events, token_address, chain)
                    if raw_price:
                        price = raw_price * eth_price
                        print(f"Got V2 price for {token_address} at block {block_number}: ${price:,.6f} USD")
                    else:
                        print(f"Could not process swap events for {token_address}")
                else:
                    print(f"No V2 swap events found for {token_address}")
            except Exception as e:
                print(f"V2 price lookup failed: {str(e)}")
        
        # 3. Try reserves (fallback)
        if not price:
            try:
                reserves_data = eth_call(
                    pair_address,
                    "0x0902f1ac", # getReserves()
                    block_number,
                    chain
                )
                if reserves_data:
                    reserve0 = int(reserves_data[2:66], 16)
                    reserve1 = int(reserves_data[66:130], 16)
                    if reserve0 > 0 and reserve1 > 0:
                        decimals0 = get_token_decimals(token_address)
                        decimals1 = get_token_decimals(WETH_ADDRESSES[chain])
                        raw_price = (reserve1 / 10**decimals1) / (reserve0 / 10**decimals0)
                        price = raw_price * eth_price
                        print(f"Got reserves price for {token_address} at block {block_number}: ${price:,.6f} USD")
                    else:
                        print(f"Zero reserves for pair {pair_address}")
                else:
                    print(f"No reserves data for pair {pair_address}")
            except Exception as e:
                print(f"Reserves lookup failed: {str(e)}")
        
        if price:
            price_cache[cache_key] = price
            return price
        
        print(f"Could not find any price for {token_address} at block {block_number} on chain {chain}")
        return None
        
    except Exception as e:
        print(f"Error getting historical price for {token_address} at block {block_number}: {str(e)}")
        return None

def process_swap_events(events: List[tuple], token_address: str, chain: str) -> Optional[float]:
    """Process swap events to find the best price"""
    try:
        if not events:
            print(f"No swap events provided for {token_address}")
            return None
            
        print(f"Processing {len(events)} swap events for {token_address}")
        prices = []
        
        for event, trace in events:
            try:
                # Skip failed transactions
                if trace and not trace.get('success', True):
                    print(f"Skipping failed transaction {event.get('transactionHash', 'unknown').hex()}")
                    continue
                    
                data = event['data'][2:]
                amount0 = int(data[:64], 16)
                amount1 = int(data[64:128], 16)
                
                if amount0 == 0 or amount1 == 0:
                    print(f"Skipping swap with zero amounts: amount0={amount0}, amount1={amount1}")
                    continue
                
                # Get token decimals
                token0_decimals = get_token_decimals(token_address)
                token1_decimals = get_token_decimals(WETH_ADDRESSES[chain])
                
                if token0_decimals is None or token1_decimals is None:
                    print(f"Could not get decimals for tokens: {token_address} or {WETH_ADDRESSES[chain]}")
                    continue
                
                # Calculate price
                price = (amount1 / 10**token1_decimals) / (amount0 / 10**token0_decimals)
                
                # Get liquidity from trace if available
                liquidity = 0
                if trace:
                    for call in trace.get('calls', []):
                        if call.get('value'):
                            liquidity += int(call['value'], 16)
                
                prices.append((price, liquidity))
                print(f"Calculated price: {price} with liquidity: {liquidity}")
                
            except Exception as e:
                print(f"Error processing swap event: {str(e)}")
                continue
        
        if not prices:
            print(f"No valid prices found from swap events for {token_address}")
            return None
            
        # Sort by liquidity and return highest liquidity price
        prices.sort(key=lambda x: x[1], reverse=True)
        best_price = prices[0][0]
        print(f"Selected best price {best_price} with highest liquidity {prices[0][1]}")
        return best_price
        
    except Exception as e:
        print(f"Error processing swap events for {token_address}: {str(e)}")
        return None

def eth_call(contract_address: str, data: str, block_number: int, chain: str) -> Optional[str]:
    """Execute a read-only contract call"""
    try:
        w3 = w3_instances.get(chain)
        if not w3:
            print(f"No web3 instance for chain {chain}")
            return None
            
        # Convert to checksum address
        try:
            contract_address = Web3.to_checksum_address(contract_address)
        except Exception as e:
            print(f"Invalid contract address format for {contract_address}: {str(e)}")
            return None
            
        # Validate block number
        try:
            if block_number != 'latest':
                block_number = int(block_number)
                if block_number < 0:
                    print(f"Invalid block number: {block_number}")
                    return None
        except Exception as e:
            print(f"Error validating block number {block_number}: {str(e)}")
            return None
            
        # Validate data format
        if not data.startswith('0x'):
            data = '0x' + data
        if not isinstance(data, str) or not all(c in '0123456789abcdefABCDEF' for c in data[2:]):
            print(f"Invalid hex data: {data}")
            return None
            
        # Make the call
        try:
            result = w3.eth.call({
                'to': contract_address,
                'data': data
            }, block_identifier=block_number)
            
            if not result:
                print(f"Empty result from eth_call to {contract_address}")
                return None
                
            return result.hex()
            
        except Exception as e:
            print(f"eth_call failed for {contract_address}: {str(e)}")
            return None
            
    except Exception as e:
        print(f"Error in eth_call: {str(e)}")
        return None

def process_token_transactions(contract: str, data: Dict, price_data: Dict) -> Dict:
    """Process transactions for a single token with detailed PnL tracking"""
    start_time = datetime.now()
    print(f"\nAnalyzing {data['symbol']} transactions...")
    
    token_results = {
        'name': data['name'],
        'symbol': data['symbol'],
        'transactions': [],
        'summary': {
            'total_bought': 0,
            'total_spent': 0,
            'total_sold': 0,
            'total_received': 0,
            'realized_pnl': 0,
            'transaction_history': []  # Detailed history of each transaction
        }
    }
    
    # Get current price
    current_price_data = price_data.get('tokens', {}).get(contract, {})
    current_price = current_price_data.get('current_price')
    
    # Track running totals
    running_balance = 0
    running_cost_basis = 0
    running_realized_pnl = 0
    
    # Process valid transactions
    valid_transactions = []
    for tx in data['transactions']:
        if not isinstance(tx, dict) or 'transaction' not in tx:
            continue
        tx_info = tx['transaction']
        if not all(k in tx_info for k in ['timestamp', 'type', 'amount']):
            continue
        if not isinstance(tx_info['amount'], (int, float)) or tx_info['amount'] <= 0:
            continue
        valid_transactions.append(tx)
    
    if not valid_transactions:
        return token_results
    
    # Sort transactions by timestamp
    valid_transactions.sort(key=lambda x: x['transaction']['timestamp'])
    
    # Process transactions
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Get block numbers
        block_futures = []
        for tx in valid_transactions:
            tx_info = tx['transaction']
            chain = tx['chain']
            future = executor.submit(get_block_by_timestamp, tx_info['timestamp'], chain)
            block_futures.append((tx, future))
        
        tx_with_blocks = []
        for tx, future in block_futures:
            try:
                block_number = future.result()
                if block_number:
                    tx_with_blocks.append((tx, block_number))
            except Exception:
                continue
        
        # Get prices
        price_futures = []
        for tx, block_number in tx_with_blocks:
            chain = tx['chain']
            future = executor.submit(get_historical_price, contract, block_number, chain)
            price_futures.append((tx, block_number, future))
        
        # Process each transaction
        for tx, block_number, future in price_futures:
            try:
                historical_price = future.result()
                tx_info = tx['transaction']
                
                # Use current price as fallback for recent transactions
                if historical_price is None and current_price:
                    if (datetime.now() - datetime.fromisoformat(tx_info['timestamp'].replace('Z', '+00:00'))).days < 7:
                        historical_price = current_price
                
                if historical_price is None:
                    continue
                
                amount = float(tx_info['amount'])
                value = amount * historical_price
                
                # Calculate transaction-specific metrics
                if tx_info['type'].lower() == 'buy':
                    # Update running totals for buy
                    running_balance += amount
                    running_cost_basis += value
                    avg_cost = running_cost_basis / running_balance if running_balance > 0 else 0
                    unrealized_pnl = (historical_price - avg_cost) * running_balance if running_balance > 0 else 0
                    
                    transaction_detail = {
                        'timestamp': tx_info['timestamp'],
                        'type': 'buy',
                        'amount': amount,
                        'price': historical_price,
                        'value': value,
                        'running_balance': running_balance,
                        'avg_cost_basis': avg_cost,
                        'unrealized_pnl': unrealized_pnl,
                        'realized_pnl': 0,
                        'block_number': block_number
                    }
                    
                else:  # sell
                    if running_balance > 0:
                        # Calculate realized PnL for this sale
                        avg_cost = running_cost_basis / running_balance
                        sale_realized_pnl = (historical_price - avg_cost) * amount
                        
                        # Update running totals for sell
                        running_balance -= amount
                        if running_balance > 0:
                            running_cost_basis = avg_cost * running_balance
                        else:
                            running_balance = 0
                            running_cost_basis = 0
                        
                        running_realized_pnl += sale_realized_pnl
                        unrealized_pnl = (historical_price - avg_cost) * running_balance if running_balance > 0 else 0
                        
                        transaction_detail = {
                            'timestamp': tx_info['timestamp'],
                            'type': 'sell',
                            'amount': amount,
                            'price': historical_price,
                            'value': value,
                            'running_balance': running_balance,
                            'avg_cost_basis': avg_cost,
                            'unrealized_pnl': unrealized_pnl,
                            'realized_pnl': sale_realized_pnl,
                            'block_number': block_number
                        }
                    else:
                        continue
                
                # Update token results
                token_results['transactions'].append(transaction_detail)
                token_results['summary']['transaction_history'].append({
                    'date': tx_info['timestamp'],
                    'action': tx_info['type'],
                    'amount': amount,
                    'price': historical_price,
                    'value': value,
                    'balance': running_balance,
                    'avg_cost': avg_cost if running_balance > 0 else 0,
                    'realized_pnl': sale_realized_pnl if tx_info['type'].lower() == 'sell' else 0,
                    'unrealized_pnl': unrealized_pnl,
                    'total_realized_pnl': running_realized_pnl
                })
                
                if tx_info['type'].lower() == 'buy':
                    token_results['summary']['total_bought'] += amount
                    token_results['summary']['total_spent'] += value
                else:
                    token_results['summary']['total_sold'] += amount
                    token_results['summary']['total_received'] += value
                
            except Exception as e:
                print(f"Error processing transaction: {str(e)}")
                continue
    
    # Calculate final PnL
    token_results['summary']['realized_pnl'] = running_realized_pnl
    
    # Add current holdings and unrealized PnL
    if running_balance > 0 and current_price:
        avg_cost = running_cost_basis / running_balance if running_balance > 0 else 0
        unrealized_pnl = (current_price - avg_cost) * running_balance
        
        token_results['summary']['current_holdings'] = running_balance
        token_results['summary']['current_price'] = current_price
        token_results['summary']['avg_cost_basis'] = avg_cost
        token_results['summary']['unrealized_value'] = running_balance * current_price
        token_results['summary']['unrealized_pnl'] = unrealized_pnl
    
    return token_results

def analyze_transactions():
    """Analyze transactions with detailed PnL tracking"""
    # Check if Web3 instances are initialized
    if not w3_instances:
        print("Error: No Web3 instances initialized. Please check your DRPC endpoints and chain configurations.")
        return

    print("\nLoading data...")
    price_data = load_current_prices()
    transactions = load_transactions()
    
    if not transactions:
        print("No transactions found to analyze")
        return
        
    token_transactions = {}
    for tx in transactions:
        if 'transaction' in tx and 'token' in tx['transaction']:
            token = tx['transaction']['token']
            contract = token['contract'].lower()
            if contract not in token_transactions:
                token_transactions[contract] = {
                    'name': token['name'],
                    'symbol': token['symbol'],
                    'transactions': []
                }
            token_transactions[contract]['transactions'].append(tx)
    
    print(f"\nAnalyzing {len(token_transactions)} tokens...")
    
    results = {}
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for contract, data in token_transactions.items():
            future = executor.submit(process_token_transactions, contract, data, price_data)
            futures.append((contract, future))
        
        for contract, future in futures:
            try:
                results[contract] = future.result()
            except Exception as e:
                print(f"Error processing {contract}: {str(e)}")
                continue
    
    if not results:
        print("No results generated. Please check the logs for errors.")
        return
        
    # Save detailed results
    output = {
        'timestamp': datetime.now().isoformat(),
        'tokens': results
    }
    
    try:
        with open('historical_prices.json', 'w') as f:
            json.dump(output, f, indent=2)
        print("\nSaved results to historical_prices.json")
    except Exception as e:
        print(f"Error saving results: {str(e)}")
    
    # Print detailed summary
    print("\nDetailed PnL Analysis:")
    total_realized_pnl = 0
    total_unrealized_value = 0
    
    for contract, data in results.items():
        if 'summary' not in data:
            continue
            
        summary = data['summary']
        history = summary.get('transaction_history', [])
        
        if not history:
            continue
            
        print(f"\n{data.get('symbol', 'Unknown')} ({data.get('name', 'Unknown')}):")
        print("\nTransaction History:")
        print("Date                   Action  Amount      Price($)    Value($)    Balance    Avg Cost($)  R.PnL($)    U.PnL($)    Total R.PnL($)")
        print("-" * 120)
        
        for tx in history:
            try:
                print(f"{tx['date']:<20} {tx['action']:<7} {tx['amount']:>10,.2f} {tx['price']:>10,.6f} {tx['value']:>10,.2f} {tx['balance']:>10,.2f} {tx['avg_cost']:>10,.6f} {tx['realized_pnl']:>10,.2f} {tx['unrealized_pnl']:>10,.2f} {tx['total_realized_pnl']:>10,.2f}")
            except Exception as e:
                print(f"Error printing transaction: {str(e)}")
                continue
        
        print("-" * 120)
        print(f"Summary:")
        print(f"Total bought: {summary.get('total_bought', 0):,.2f} tokens (${summary.get('total_spent', 0):,.2f})")
        print(f"Total sold: {summary.get('total_sold', 0):,.2f} tokens (${summary.get('total_received', 0):,.2f})")
        print(f"Realized PnL: ${summary.get('realized_pnl', 0):,.2f}")
        
        if 'current_holdings' in summary:
            print(f"Current holdings: {summary['current_holdings']:,.2f} tokens")
            print(f"Average cost basis: ${summary.get('avg_cost_basis', 0):,.6f}")
            print(f"Current price: ${summary.get('current_price', 0):,.6f}")
            print(f"Unrealized value: ${summary.get('unrealized_value', 0):,.2f}")
            print(f"Unrealized PnL: ${summary.get('unrealized_pnl', 0):,.2f}")
            total_unrealized_value += summary.get('unrealized_value', 0)
        
        total_realized_pnl += summary.get('realized_pnl', 0)
        print()
    
    print("\nPortfolio Summary:")
    print(f"Total Realized PnL: ${total_realized_pnl:,.2f}")
    print(f"Total Unrealized Value: ${total_unrealized_value:,.2f}")
    print(f"Total Portfolio Value: ${(total_realized_pnl + total_unrealized_value):,.2f}")

if __name__ == "__main__":
    analyze_transactions() 