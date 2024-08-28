from web3 import Web3
import json
import sys

# Read the JSON payload from command-line argument
var1 = sys.argv[1]
var2 = sys.argv[2]
var3 = sys.argv[3]
var4 = sys.argv[4]
var5 = sys.argv[5]
var6 = sys.argv[6]
var7 = sys.argv[7]



# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('HTTP://192.168.1.80:8546'))
# Set the account and private key for signing transactions
account_address = "0xd5e47682bf66a3b34ba04ddda399827c575b7359"
private_key = "0x9fd3cc32a98927b2f7d74090a91b36b005a173976c1b00ea5d45aad3d9e2685c"
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

# Create transaction
transaction = contract.functions.addCandidate(var1,var2,var3,var4,var5,var6,var7).build_transaction({
    'from': account_address,
    'gas': 2000000,
    'gasPrice': w3.to_wei('500', 'gwei'),
    'nonce': w3.eth.get_transaction_count(account_address),
})

# Sign transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
#signed_txn = w3.eth.sign_transaction(dict(nonce=w3.eth.get_transaction_count(w3.eth.coinbase),maxFeePerGas=2000000000,maxPriorityFeePerGas=1000000000,gas=100000,to=account_address))
# Send the signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)



# Wait for the transaction to be mined
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Print the transaction receipt
print("Transaction receipt:")
print(tx_receipt)


