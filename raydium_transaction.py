from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solders.signature import Signature

from pool_keys import get_pool_keys
from buy_sell import buy, sell
from verify_txn import verify_transaction
from constants import WSOL

# from solana.rpc.api import Keypair
from solders.keypair import Keypair

HTTP_ENDPOINT = "https://api.mainnet-beta.solana.com"
WS_ENDPOINT = "wss://api.mainnet-beta.solana.com"

# Wallet Key
WALLET_KEY = ""


class Raydium:
    GAS_LIMIT = 200000
    GAS_PRICE = 25000

    def __init__(self, wallet_key: str, rpc_url: str = HTTP_ENDPOINT) -> None:

        self.client = Client(rpc_url)
        self.payer = Keypair.from_base58_string(wallet_key)
        self.my_wallet = self.payer.pubkey()


    def verify_txn(self, signature: str) -> bool:

        verification = verify_transaction(self.client, signature)

        return verification


    def get_pool_data(self, amm_id: str) -> dict:

        amm_id = Pubkey.from_string(amm_id)

        pool_keys = get_pool_keys(self.client, amm_id)

        return pool_keys


    def buy_swap(self, amm_id: str, amount: float, pool_keys=None) -> Signature:

        pool_keys = self.get_pool_data(amm_id) if not pool_keys else pool_keys

        if pool_keys:
            txn = buy(self.client, pool_keys['base_mint'], self.payer, amount, pool_keys, self.GAS_LIMIT,
                      self.GAS_PRICE)

            return txn


    def sell_swap(self, amm_id: str, amount: float, pool_keys=None) -> Signature:

        pool_keys = self.get_pool_data(amm_id) if not pool_keys else pool_keys

        if pool_keys:
            txn = sell(self.client, pool_keys['base_mint'], self.payer, amount, pool_keys, self.GAS_LIMIT,
                       self.GAS_PRICE)

            return txn




