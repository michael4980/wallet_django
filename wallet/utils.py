from web3 import Web3
from .models import Wallet

def create_wallet():
    web = Web3()
    account = web.eth.account.create()
    wallet = Wallet(currency='ETH', public_key=account.address, private_key=account._private_key.hex())
    wallet.save()
    return wallet.id
