from web3 import Web3
from web3.middleware import geth_poa_middleware

import json
import sys
import time


# Connect to the Ethereum node
#w3 = Web3(Web3.HTTPProvider('HTTP://192.168.1.80:8546'))
w3 = Web3(Web3.HTTPProvider('HTTP://172.28.96.1:7545'))


w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# Set the account and private key for signing transactions
account_address = "0x217F14279c8313EB872fc3222DA6553e0C62282C"
private_key = "0x7a0c8eba5a872e055da3ed1730b915825a4c8d05160b8093bdd8a7ce16e3dbe8"
# Set the contract address and ABI
contract_address = "0x13250E8fEaD5b191004DBbf976283d69F24b6b6C"
contract_abi = [
    {
      "constant": True,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "candidates",
      "outputs": [
        {
          "internalType": "string",
          "name": "var1",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "var2",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "var3",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "var4",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "var5",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "var6",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "var7",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "candidatesCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "voters",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "internalType": "string",
          "name": "_var1",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_var2",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_var3",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_var4",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_var5",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_var6",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_var7",
          "type": "string"
        }
      ],
      "name": "addCandidate",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_candidateId",
          "type": "uint256"
        }
      ],
      "name": "vote",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
# Create contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

               



# Get the latest block number
latest_block = w3.eth.get_block('latest')
print(f'Latest Block: {latest_block} ')
#print(latest_block)
# Get the block number of the block 100 blocks ago
block_number = latest_block.number - 100
print(f'Before 100 Blocks: {block_number}')

block = w3.eth.get_block(block_number)
timestamp_100_blocks_ago = block.timestamp

# Calculate the number of transactions in the last 100 blocks
num_transactions = 100
for i in range(block_number, latest_block.number + 1):
    block = w3.eth.get_block(i)
    num_transactions += len(block.transactions)

# Calculate the throughput
time_elapsed = latest_block.timestamp - timestamp_100_blocks_ago
throughput = num_transactions / time_elapsed
print(f'No of Transactions: {num_transactions}')
print(f'Time Elapsed: {time_elapsed}')
print(f'Throughput in the last 100 blocks: {throughput:.5f} transactions per second')



