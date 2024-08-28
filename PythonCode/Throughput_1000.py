from web3 import Web3, EthereumTesterProvider
from web3.middleware import geth_poa_middleware
import json
import time


#w3 = Web3(Web3.HTTPProvider('HTTP://172.28.96.1:7545'))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# Set the account and private key for signing transactions
#account_address = "0x217F14279c8313EB872fc3222DA6553e0C62282C"
#private_key = "0x7a0c8eba5a872e055da3ed1730b915825a4c8d05160b8093bdd8a7ce16e3dbe8"
# Set the contract address and ABI
#contract_address = "0x13250E8fEaD5b191004DBbf976283d69F24b6b6C"



# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('http://192.168.1.80:8546'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Set the account and private key for signing transactions
account_address = "0xC5C0d86106D6fb21A0747eB0d5637d9A8d219856"
private_key = "0x9fd3cc32a98927b2f7d74090a91b36b005a173976c1b00ea5d45aad3d9e2685c"

# Create contract instance (you may need to define contract_address and contract_abi)
contract_address = "0xAB5E4c096bd7002e699A4C4eAeB77905C05Ee509"
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
contract = w3.eth.contract(address=contract_address, abi=contract_abi)




# Define the number of transactions to send
num_transactions = 100

# Store the starting time
start_time = time.time()

# Send 1000 transactions to the Ethereum network
for i in range(num_transactions):
    try:
        # Get the current nonce within the loop to ensure it's unique for each transaction
        current_nonce = w3.eth.get_transaction_count(account_address, 'pending')

        # Build the transaction
        transaction_data = contract.functions.addCandidate("vars","vars2","var3","var4","var5","var6","var7").build_transaction({
            'from': account_address,
            'value': 0,
            'gas': 200000,
            'gasPrice': w3.eth.gas_price,
            'nonce': current_nonce,
            'chainId': 5777
        })

        # Sign the transaction
        signed_transaction = w3.eth.account.sign_transaction(transaction_data, private_key)

        # Send the transaction
        tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        # Print the hash for tracking (uncomment for debugging)
        # print(f'Transaction {i+1} sent with hash: {tx_hash}')

    except Exception as e:
        print(f'Transaction {i+1} failed: {e}')


# Calculate the total time taken for 1000 transactions
end_time = time.time()
total_time = end_time - start_time

# Calculate latency (average time per transaction)
latency = total_time / num_transactions

# Calculate throughput (transactions per second)
throughput = num_transactions / total_time

# Print the results
print(f"Total time taken for {num_transactions} transactions: {total_time} seconds")
print(f"Average latency per transaction: {latency} seconds")
print(f"Throughput: {throughput} transactions per second")
