from web3 import Web3
from loguru import logger
from client import Client
from config import CONTRACT_ABI, private_key
from utils import read_json
from models import XAI


class Mint:

    def __init__(self, client: Client):
        self.client = client

        if self.client.network == XAI:
            self.router_address = Web3.to_checksum_address('0x9d600c4b597E6d58cbCe8CDb6d9f6A57d5aF28c9')

    router_abi = read_json(CONTRACT_ABI)

    def start_mint(self):
        contract = self.client.w3.eth.contract(
            abi=Mint.router_abi,
            address=self.router_address
        )
        try:
            tx = self.client.send_transaction(
                to=self.router_address,
                data=contract.encodeABI('buyNftNative',
                                        args=(
                                            self.client.address,
                                            '0xf46ef9414cD1547E883761c54Cb9939060D05cfa'
                                        )),
            )

            success_tx = self.client.verif_tx(tx)

            if success_tx:
                logger.info(f"{self.client.network.explorer}/tx/{tx.hex()}")
                logger.success(f'[{self.client.address}][Mint NFT] Successfully mint NFT')
            else:
                logger.error(f'[{self.client.address}][Mint NFT] mint NFT error')
        except Exception as err:
            logger.error(f'[{self.client.address}][Mint NFT] mint NFT error: {type(err).__name__} {err}')
