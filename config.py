import os
import sys
from pathlib import Path

# Создаем объект Path для директории
if getattr(sys, 'frozen', False):
    directory_path = Path(sys.executable).parent.absolute()
else:
    directory_path = Path(__file__).parent.parent.absolute()

# Here edit your path if you have errors
ABIS_DIR = os.path.join(directory_path, 'ARB XAI GAMES', 'abis')

CONTRACT_ABI = os.path.join(ABIS_DIR, 'contract_abi.json')
TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')

transactions = 2

private_key = ''

PAUSA_MAX = 5 # сон
PAUSA_MIN = 2