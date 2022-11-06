from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from Crypto.Hash import SHA256
from AccountModel import AccountModel
from Node import Node
import sys

if __name__ == "__main__":
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])
    keyfile = None
    if len(sys.argv) > 4:
        keyfile = sys.argv[4]

    node = Node(ip, port, keyfile)
    node.startP2P()
    node.startAPI(apiPort)