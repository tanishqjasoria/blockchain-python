import hashlib
import json
from time import time




class Blockchain(object):
  """
  This class is responsible form managing the chain. It will store
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

    # Create the genesis block
    self.new_block(previous_hash=1, proof=100)



  def new_block(self, proof, previous_hash=None):
    """
    Create a new Block in the Blockchain
    :param proof: The proof given by the Proof of Work algorithm
    :param previous_hash: Hash of previous Block
    :return: New Block
    """

    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
    }

    # Reset the current list of transactions
    self.current_transactions = []

    self.chain.append(block)
    return block



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

    return self.chain[-1]



  def proof_of_work(self, last_proof):
    """
    Simple Proof of Work Algorithm:
     - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
     - p is the previous proof, and p' is the new proof
    :param last_proof: value of last Proof
    :return: new value of Proof of work
    """

    proof = 0
    while self.valid_proof(last_proof, proof) is False:
      proof += 1

    return proof



  @staticmethod
  def valid_proof(last_proof, proof):
    """
    Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
    :param last_proof: value of last Proof
    :param proof: current possible value of Proof
    :return: True if correct, False if not.
    """

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"
  
