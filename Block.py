from hashlib import sha256
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        """
        index: id of block
        transactions: list transactions
        timestamp: time to create a block
        previous_hash: hash of previous block
        """
        self.index = index
        self.transactions = transactions
        self.timestamp= timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


