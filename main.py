from mint import Mint
from sys import stderr
from models import XAI
from config import private_key, transactions
from utils import sleeping
from loguru import logger
from client import Client

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")


def start():
    i = 0

    logger.info(f'Транзакция: {i + 1}/{transactions}')

    while i < transactions:

        client = Client(private_key=private_key, network=XAI)
        mint = Mint(client=client)
        mint.start_mint()
        i += 1
        sleeping()


if __name__ == '__main__':
    start()
