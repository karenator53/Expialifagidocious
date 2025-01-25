from web3 import Web3
import json

# Connect to Sonic RPC
w3 = Web3(Web3.HTTPProvider('https://rpc.soniclabs.com'))

# Pair ABI - minimal version with just factory() function
PAIR_ABI = json.dumps([{
    "constant": True,
    "inputs": [],
    "name": "factory",
    "outputs": [{"name": "", "type": "address"}],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
}])

# List of known pairs for each DEX
PAIRS = {
    'Equalizer': '0x3E6daa42268a5097De68ab39e48B860B9B55f589',  # THC/wS
    'Wagmi': '0x8F76E0dEB376D81FD75028d47De0DA7af0a5547E',     # WAGMI/Anon
    'Shadow': '0x1f4eFC47e5A5Ab6539d95A76e2dDE6d74462acEa',    # GOGLZ/wS
    'Metropolis': '0xD55BB10BA2b5f2Eb0E1cbeB8191615de699b56a8', # LAIRA/wS
    'SwapX': '0xbeca246A76942502f61bFe88F60bbc87DaFefe80'      # SWPx/wS
}

def get_factory_address(pair_address):
    """Get factory address from pair contract"""
    pair_contract = w3.eth.contract(address=pair_address, abi=PAIR_ABI)
    try:
        factory = pair_contract.functions.factory().call()
        return factory
    except Exception as e:
        print(f"Error getting factory for {pair_address}: {e}")
        return None

def main():
    print("Querying factory addresses for known pairs...")
    for dex, pair in PAIRS.items():
        factory = get_factory_address(pair)
        if factory:
            print(f"{dex} Factory: {factory} (from pair {pair})")
        else:
            print(f"{dex}: Failed to get factory address")

if __name__ == "__main__":
    main()