import logging
from web3 import Web3

logging.basicConfig(level=logging.INFO)

# 1) DRPC endpoints for your chains
DRPC_ENDPOINTS = {
    'ethereum': 'https://lb.drpc.org/ogrpc?network=ethereum&dkey=At-n0kIQ5kxdp0Dgm1C_C8fog4Lf1RYR74rJKuk0h5Qw',
    'base': 'https://lb.drpc.org/ogrpc?network=base&dkey=At-n0kIQ5kxdp0Dgm1C_C8fog4Lf1RYR74rJKuk0h5Qw',
    'sonic': 'https://lb.drpc.org/ogrpc?network=sonic&dkey=At-n0kIQ5kxdp0Dgm1C_C8fog4Lf1RYR74rJKuk0h5Qw'
}

# 2) Factory addresses (make sure these are truly FACTORY addresses, not routers!)
FACTORY_ADDRESSES = {
    # Example: Ethereum
    'ethereum': [
        # Uniswap V2 factory
        '0x5C69BEE701EF814A2B6a3EDD4B1652CB9CC5aA6f',
        # Uniswap V3 factory
        '0x1F98431c8aD98523631AE4A59f267346ea31F984'
    ],
    # Example: Base
    'base': [
        # BaseSwap V2
        '0x8909Dc15e40173Ff4699343b6eB8132c65e18eC6',
        # Uniswap V3
        '0x633a093C9e94f64500FC8fCBB48e90dd52F6668F',
        # ... etc ...
    ],
    # Example: "sonic" chain (replace with correct factory addresses if needed)
    'sonic': [
        '0xF6239BaE7E0A6e89745B5C87011B7A641916b52d',  # Suppose V2
        '0x1F98431c8aD98523631AE4A59f267346ea31F984',  # Suppose V3
    ],
}

# 3) Known token addresses to test for pairs.
#    Ideally, pick a stablecoin or WETH on each chain so we can do a real test.
WETH_ADDRESSES = {
    'ethereum': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    'base':     '0x4200000000000000000000000000000000000006',
    'sonic':    '0x5300000000000000000000000000000000000004',
}

# Some widely used stablecoins (feel free to adjust for each chain)
STABLECOINS = {
    'ethereum': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606Eb48',  # USDC
    'base':     '0x8ede1712b7A55b39ccBd3de4E0F7BfD29eCf78Fa',  # USDbC on Base
    'sonic':    '0x0000000000000000000000000000000000000000',  # ?? Replace if your chain has a stable
}

# V2 factory ABI (minimal)
V2_FACTORY_ABI = [
    {
        "name": "getPair",
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"}
        ],
        "outputs": [{"internalType": "address", "name": "pair", "type": "address"}],
    }
]

# V3 factory ABI (minimal)
V3_FACTORY_ABI = [
    {
        "name": "getPool",
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint24",  "name": "fee",    "type": "uint24"}
        ],
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
    }
]

# Typical Uniswap V3 fee tiers
V3_FEE_TIERS = [500, 3000, 10000]  # 0.05%, 0.3%, 1%, etc.

def main():
    logging.info("===== Step 1: Test connectivity =====")
    w3_instances = {}
    for chain, endpoint in DRPC_ENDPOINTS.items():
        w3 = Web3(Web3.HTTPProvider(endpoint))
        if w3.is_connected():
            w3_instances[chain] = w3
            logging.info(f"[OK] Connected to {chain} at {endpoint}")
        else:
            logging.warning(f"[FAIL] Could NOT connect to {chain} at {endpoint}")
    print()

    logging.info("===== Step 2: Test each factory for V2 or V3 presence =====")
    # We'll check each factory address to see if calling getPair or getPool reverts
    # or returns a valid value. This helps identify whether it is truly a V2 or V3 factory.
    # In many DEX contracts, if you call the wrong function, you'll get an immediate revert or empty data.

    for chain, factories in FACTORY_ADDRESSES.items():
        if chain not in w3_instances:
            logging.warning(f"[SKIP] Not connected to {chain}, cannot test factories.")
            continue
        w3 = w3_instances[chain]
        logging.info(f"--- Factories on {chain} ---")

        for factory_addr in factories:
            factory_addr = Web3.to_checksum_address(factory_addr)
            logging.info(f"Factory: {factory_addr}")
            # Try V2 getPair
            is_v2 = False
            try:
                factory_v2 = w3.eth.contract(address=factory_addr, abi=V2_FACTORY_ABI)
                # We'll just call getPair for two arbitrary addresses, or WETH + WETH:
                test_pair = factory_v2.functions.getPair(
                    '0x0000000000000000000000000000000000000001',
                    '0x0000000000000000000000000000000000000002'
                ).call()
                # If it didn't revert, it likely is a V2 factory or has the function stub
                # You might still get '0x0000...' as result, which is normal for a nonexistent pair
                is_v2 = True
                logging.info("  [OK] getPair() call succeeded. This looks like a V2 factory.")
            except Exception as e:
                logging.info("  [INFO] getPair() call failed. Likely not V2 or incompatible.")
            
            # Try V3 getPool
            is_v3 = False
            try:
                factory_v3 = w3.eth.contract(address=factory_addr, abi=V3_FACTORY_ABI)
                test_pool = factory_v3.functions.getPool(
                    '0x0000000000000000000000000000000000000001',
                    '0x0000000000000000000000000000000000000002',
                    500
                ).call()
                # If it didn't revert, it likely is a V3 factory
                is_v3 = True
                logging.info("  [OK] getPool() call succeeded. This looks like a V3 factory.")
            except Exception as e:
                logging.info("  [INFO] getPool() call failed. Likely not V3 or incompatible.")
            
            if not is_v2 and not is_v3:
                logging.warning("  [WARN] Neither getPair nor getPool worked. This may not be a valid factory!")
        print()

    logging.info("===== Step 3: Test known WETH–stable pair on each chain for each factory =====")
    # If the chain is recognized, we attempt to see if the known WETH–stable pair exists.
    # For V2 factories, we'll just do getPair(tokenA, tokenB).
    # For V3 factories, we’ll do getPool(tokenA, tokenB, fee) with typical fee tiers.
    # We expect at least one of these calls to yield a non-zero address on a popular factory.
    for chain, factories in FACTORY_ADDRESSES.items():
        if chain not in w3_instances:
            continue
        w3 = w3_instances[chain]
        logging.info(f"--- Checking WETH–stable on {chain} ---")

        weth = WETH_ADDRESSES.get(chain)
        stable = STABLECOINS.get(chain)
        if not weth or not stable or stable.lower() == '0x0000000000000000000000000000000000000000':
            logging.warning(f"[SKIP] No valid WETH/stable addresses set for {chain}")
            continue
        
        logging.info(f"Testing pair/pool for WETH={weth} & stable={stable}")

        # Check each factory
        for factory_addr in factories:
            factory_addr = Web3.to_checksum_address(factory_addr)
            logging.info(f"Factory: {factory_addr}")
            # V2 attempt:
            factory_v2 = w3.eth.contract(address=factory_addr, abi=V2_FACTORY_ABI)
            try:
                pair_addr = factory_v2.functions.getPair(weth, stable).call()
                if pair_addr != '0x0000000000000000000000000000000000000000':
                    logging.info(f"  [OK] getPair() => {pair_addr}")
                else:
                    logging.info("  [INFO] getPair() => zero address (no V2 pair found).")
            except Exception as e:
                logging.debug(f"  [DEBUG] V2 getPair() call error: {e}")

            # V3 attempt:
            factory_v3 = w3.eth.contract(address=factory_addr, abi=V3_FACTORY_ABI)
            for fee in V3_FEE_TIERS:
                try:
                    pool_addr = factory_v3.functions.getPool(weth, stable, fee).call()
                    if pool_addr != '0x0000000000000000000000000000000000000000':
                        logging.info(f"  [OK] getPool(fee={fee}) => {pool_addr}")
                except Exception as e:
                    # Usually means "function not found" or "execution reverted"
                    logging.debug(f"  [DEBUG] V3 getPool(fee={fee}) call error: {e}")
        print()

    logging.info("===== Testing Complete. Review the logs above for details. =====")


if __name__ == "__main__":
    main()
