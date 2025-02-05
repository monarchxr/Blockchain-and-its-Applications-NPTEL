# Learning how to implement a simple blockchain

#import library
import hashlib

#create a block class
class Block:
    #create a constructor for block
    def __init__(self,data,prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    #create a method to calculate hash using SHA-256

    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(self.data.encode('utf-8'))

        return sha.hexdigest()
    

#create a blockchain class
class Blockchain:
    #create a constructor for blockchain

    def __init__(self):
        self.chain = [self.create_genesis_block()]


    #create a method to create the first block in the blockchain, also known as a genesis block

    def create_genesis_block(self):

        return Block("Genesis Block", "0")
    
    #create a method that creates a new block and adds it to the blockchain, aka list

    def add_block(self,data):
        prev_block = self.chain[-1]

        new_block = Block(data, prev_block.hash)

        self.chain.append(new_block)

if __name__ == "__main__":

    print("Initializing the blockchain")

    blockchain = Blockchain()

    size = int(input("Enter how many blocks to add to the blockchain: "))

    for i in range(0,size):
        blockchain.add_block("Block %d"%(i+1))

    print("Current blockchain: \n")

    for block in blockchain.chain:
        print("data: ", block.data)
        print("previous hash: ", block.prev_hash)
        print("hash: ", block.hash)
