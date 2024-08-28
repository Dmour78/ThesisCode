
from web3 import Web3
from web3.middleware import geth_poa_middleware
import time

# Connect to your Ethereum node
w3 = Web3(Web3.HTTPProvider('HTTP://192.168.1.80:8546'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

account_address = "0xC5C0d86106D6fb21A0747eB0d5637d9A8d219856"
private_key = "0x9fd3cc32a98927b2f7d74090a91b36b005a173976c1b00ea5d45aad3d9e2685c"
# Set the contract address and ABI
contract_address = "0x639f730aa620d264d456f7C9b64c45D4f55fa2f4"
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
# Function to send a transaction and measure latency
def measure_latency():
    start_time = time.time()
    # Create a transaction (replace with your transaction details)
    transaction = contract.functions.addCandidate("var1", "var2", "var3", "var4", "var5", "var6", "var7").build_transaction({
            'from': "0xC5C0d86106D6fb21A0747eB0d5637d9A8d219856",
            'gas': 2000000,
            'gasPrice': w3.to_wei('500', 'gwei'),
            'nonce': w3.eth.get_transaction_count(account_address),
            })
    tx_hash = w3.eth.send_transaction(transaction)
    # Wait for the transaction to be mined
    w3.eth.waitForTransactionReceipt(tx_hash)
    end_time = time.time()
    latency = end_time - start_time
    return latency

# Function to measure throughput
def measure_throughput(num_transactions, measurement_duration):
    start_time = time.time()
    transactions = []
    for _ in range(num_transactions):
      latency = measure_latency()
      transactions.append(latency)
      if time.time() - start_time >= measurement_duration:
         break
      end_time = time.time()
      throughput = len(transactions) / (end_time - start_time)
      return throughput, transactions

if __name__ == "__main__":
    num_transactions = 100  # Number of transactions to measure throughput
    measurement_duration = 60  # Measurement duration in seconds
    
    throughput, latencies = measure_throughput(num_transactions, measurement_duration)
    
    print(f"Throughput: {throughput} TPS")
    print(f"Average Latency: {sum(latencies) / len(latencies)} seconds")

