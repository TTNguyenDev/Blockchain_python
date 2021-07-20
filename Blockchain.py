from Block import Block
import time

class Blockchain:
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False #Check contain unconfirm trans

        last_block = self.last_block

        new_block = Block(last_block.index + 1, 
                self.unconfirmed_transactions,
                time.time(),
                last_block.previous_hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

    @property
    def last_block(self):
        return self.chain[-1]
    
    def add_block(self, block, proof):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False
        
        if not is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)

        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * difficulty) and 
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        block.nonce = 0

        compute_hash = block.compute_hash()

        while not compute_hash.startswith('0' * difficulty):
            block.nonce += 
            compute_hash = block.compute_hash()

        return compute_hash


