import hashlib
import json





class Blockchain(object):
    """
    This class is reponsible form managing the chain. It will store
    transactions and have some helper methods for adding new blocks
    to the chain.

    Each block has an index, a timestamp, a lis of transactions,
    a proof, and the hash of the previous Block

    Structure of the block:
    block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b16...."
    }
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []



    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass



    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append(
            {
                'sender' : sender,
                'recipient' : recipient,
                'amount' : amount,
            }
        )

        return self.last_block['index'] + 1



    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        :return: Hash of Block
        """

        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
