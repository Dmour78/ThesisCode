from web3 import Web3
from web3.middleware import geth_poa_middleware

import json
import sys
import time


# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('HTTP://192.168.1.80:8546'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# Set the account and private key for signing transactions
account_address = "0xD5E47682Bf66A3b34BA04dDdA399827c575B7359"
private_key = "0xaff0414b1352c4a2645600a9829df27027b20e435aeed901d2af2ac17f8802b1"
# Set the contract address and ABI
contract_address = "0xaeB89e342cE674e0410e10C2fc09FF0E2dC063b3"
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

               



def on_message(client, userdata, msg):
	payload = msg.payload.decode('utf-8')
	variables = payload.split(',')
	var1, var2, var3, var4, var5, var6, var7 = variables
num_transactions = 1000000
start_time = time.time()
print(f"Start Time: {start_time}")

for _ in range(num_transactions):
  transaction = contract.functions.addCandidate("var1","var2","var3","var4","var5","var6","var7").build_transaction({
	  'from': account_address,
    'gas': 200000,
    'gasPrice': w3.to_wei('500', 'gwei'),
    'nonce': w3.eth.get_transaction_count(account_address),
    })
  signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
  tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
  tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
  print(tx_receipt)
end_time = time.time()
print(f"End Time: {end_time}")
# Calculate latency
latency = (end_time - start_time) / num_transactions
print(f"Latency per transaction: {latency} mili seconds")
# Calculate throughput
throughput = num_transactions / (end_time - start_time)
print(f"Throughput: {throughput} transactions per second")
# Print the transaction receipt
print("Transaction receipt:")
# Connect to a Geth node using HTTP provider

# Get the latest block number
latest_block = w3.eth.get_block('latest')
print(latest_block)
# Get the block number of the block 100 blocks ago
block_number = latest_block.number - 1000
block = w3.eth.get_block(block_number)
timestamp_100_blocks_ago = block.timestamp

# Calculate the number of transactions in the last 100 blocks
num_transactions = 0
for i in range(block_number, latest_block.number + 1):
    block = w3.eth.get_block(i)
    num_transactions += len(block.transactions)

# Calculate the throughput
time_elapsed = latest_block.timestamp - timestamp_100_blocks_ago
throughput = num_transactions / time_elapsed

print(f'Throughput in the last 100 blocks: {throughput:.5f} transactions per second')



