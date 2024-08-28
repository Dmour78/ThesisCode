from web3 import Web3
from web3.middleware import geth_poa_middleware
import paho.mqtt.client as mqtt
import json
import sys
import time

MQTT_ADDRESS = "192.168.1.80"
MQTT_USER = "mosq"
MQTT_PASSWORD = "Jordan@2020"
MQTT_TOPIC = "ESP32Topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    payload = msg.payload.decode("utf-8")
    try:
        data = json.loads(payload)
        if len(data) == 8:
            # Extract and print the variables
            var1 = data.get("Var1")
            var2 = data.get("Var2")
            var3 = data.get("Var3")
            var4 = data.get("Var4")
            var5 = data.get("Var5")
            var6 = data.get("Var6")
            var7 = data.get("Var7")
            print(var1, var2, var3, var4, var5, var6, var7)
            w3 = Web3(Web3.HTTPProvider('HTTP://192.168.1.80:8546'))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            # Set the account and private key for signing transactions
            account_address = "0xD5E47682Bf66A3b34BA04dDdA399827c575B7359"
            private_key = "0xaff0414b1352c4a2645600a9829df27027b20e435aeed901d2af2ac17f8802b1"
            # Set the contract address and ABI
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
                # Create contract instance 'nonce': w3.eth.get_transaction_count(account_address),
            contract = w3.eth.contract(address=contract_address, abi=contract_abi)
            start_time = time.time()
            current_nonce = w3.eth.get_transaction_count(account_address, 'pending')
            transaction = contract.functions.addCandidate(var1,var2,var3,var4,var5,var6,var7).build_transaction({
                'from': account_address,
                'gas': 200000,
                'gasPrice': w3.to_wei('5000', 'gwei'),
                'nonce': current_nonce,
                })
            signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            end_time = time.time()
            latency = end_time - start_time
            print(start_time)
            print(end_time)
            print(latency)                
            
            
        else:
            print("Received JSON with incorrect number of variables")
    except json.JSONDecodeError:
        print("Received invalid JSON")

# Create an MQTT client instance tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)print(tx_receipt)
client = mqtt.Client()

# Set the username and password for authentication (if required by the broker)
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# Set the callbacks for connection and message reception
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_ADDRESS, 1883)

# Start the MQTT network loop to handle incoming messages
client.loop_start()

# Keep the script running to continue receiving messages
while True:
    pass
