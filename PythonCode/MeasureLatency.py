from web3 import Web3
import json
import sys
import time


# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('HTTP://192.168.1.6:8544'))
# Set the account and private key for signing transactions
account_address = "0xC5C0d86106D6fb21A0747eB0d5637d9A8d219856"
private_key = "0x9fd3cc32a98927b2f7d74090a91b36b005a173976c1b00ea5d45aad3d9e2685c"
# Set the contract address and ABI
contract_address = "0x81230a01f1A806309f76fc6E270652ec88cD0bd7"
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
num_transactions = 1000
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
start_time = time.time()
def send_transactions(num_transactions):
    for _ in range(num_transactions):
        transaction = contract.functions.addCandidate("var1", "var2", "var3", "var4", "var5", "var6", "var7").build_transaction({
            'from': account_address,
            'gas': 2000000,
            'gasPrice': w3.to_wei('500', 'gwei'),
            'nonce': w3.eth.get_transaction_count(account_address),
        })
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print("Transaction receipt:")
        print(tx_receipt)
end_time = time.time()
latency = (end_time - start_time) / num_transactions
print(f"Latency per transaction: {latency} seconds")
throughput = num_transactions / (end_time - start_time)
print(f"Throughput: {throughput} transactions per second")
# Define the number of transactions to send

# Send transactions and measure latency and throughput
send_transactions(num_transactions)

