'''
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. 
Each block contains some information and how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

We can break the blockchain down into three main parts.

First is the information hash:

import hashlib

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
     
We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:
'''

import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, o_str):
        sha = hashlib.sha256()
        hash_str = o_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return str(self.timestamp) + str(' | ') \
            + str(self.data) + str(' | ') + str(self.previous_hash) \
            + str(' | ') + str(self.hash)

class BlockChain(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if data is None or data == '':
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)

        return

    def to_List(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out


# Test case for Block
b1 = Block(datetime.datetime.utcnow(), 'First block b1', 0)
b2 = Block(datetime.datetime.utcnow(), 'Second block b2', b1)
b3 = Block(datetime.datetime.utcnow(), 'Third block b3', b2)

# Test case for BlockChain
block_chain = BlockChain()
block_chain.append('First block chain bc1')
block_chain.append('Second block chain bc2')
block_chain.append('Third block chain bc3')

# Tests
print('The b1 data: ', b1.data)
print('The b1 hash value: ', b1.hash)
print('The b1 timestamp: ', b1.timestamp)
print('The previous block data of b2: ', b2.previous_hash.data)
print('The block_chain tail data: ', block_chain.tail.data)
print('The block_chain previous hash data: ', block_chain.tail.previous_hash)

'''
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. 
All of this will help you build up to a simple but full blockchain implementation!
'''

