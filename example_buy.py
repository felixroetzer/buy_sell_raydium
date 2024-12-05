from raydium_transaction import Raydium

RPC_URL = "https://api.mainnet-beta.solana.com"  # Solana Mainnet RPC
PRIVATE_KEY = "YOUR_PRIVATE_KEY" # Enter your private key
POOL_ID = "POOL_ID" # Can find the address on dexscreener on the coin page under "Pair", e.g. "93tjgwff5Ac5ThyMi8C4WejVVQq4tuMeMuYW1LEYZ7bu" for CHILLGUY pair.
BUY_AMOUNT = 0.005  # Amount in quote asset (SOL)

raydium = Raydium(wallet_key=PRIVATE_KEY, rpc_url=RPC_URL)

try:
    txn_signature = raydium.buy_swap(amm_id=POOL_ID, amount=BUY_AMOUNT)
    print(f"Buy transaction was successful, view on SolScan: https://solscan.io/tx/{txn_signature}")
except Exception as e:
    print(f"Buy transaction failed: {e}")
