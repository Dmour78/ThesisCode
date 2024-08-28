from web3 import Web3
from web3.middleware import geth_poa_middleware
import paho.mqtt.client as mqtt
import json
import sys

MQTT_TOPIC = "ESP32Topic"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    var1 = sys.argv[1]
    var2 = sys.argv[2]
    var3 = sys.argv[3]
    var4 = sys.argv[4]
    var5 = sys.argv[5]
    var6 = sys.argv[6]
    var7 = sys.argv[7]
    w3 = Web3(Web3.HTTPProvider("HTTP://192.168.1.80:8546"))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    # Set the account and private key for signing transactions
    account_address = "0xD5E47682Bf66A3b34BA04dDdA399827c575B7359"
    private_key = "0xaff0414b1352c4a2645600a9829df27027b20e435aeed901d2af2ac17f8802b1"
    # Set the contract address and ABI
    contract_address = "0xb34f3EAb199A643c45D755f2A5671957412bE727"
    contract_abi = [
        {
            "constant": True,
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "candidates",
            "outputs": [
                {"internalType": "string", "name": "var1", "type": "string"},
                {"internalType": "string", "name": "var2", "type": "string"},
                {"internalType": "string", "name": "var3", "type": "string"},
                {"internalType": "string", "name": "var4", "type": "string"},
                {"internalType": "string", "name": "var5", "type": "string"},
                {"internalType": "string", "name": "var6", "type": "string"},
                {"internalType": "string", "name": "var7", "type": "string"},
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "candidatesCount",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "voters",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "string", "name": "_var1", "type": "string"},
                {"internalType": "string", "name": "_var2", "type": "string"},
                {"internalType": "string", "name": "_var3", "type": "string"},
                {"internalType": "string", "name": "_var4", "type": "string"},
                {"internalType": "string", "name": "_var5", "type": "string"},
                {"internalType": "string", "name": "_var6", "type": "string"},
                {"internalType": "string", "name": "_var7", "type": "string"},
            ],
            "name": "addCandidate",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "uint256", "name": "_candidateId", "type": "uint256"}
            ],
            "name": "vote",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]


# Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    num_transactions = 1

    for _ in range(num_transactions):
     transaction = contract.functions.addCandidate(
        var1, var2, var3, var4, var5, var6, var7
       ).build_transaction(
       {
            "from": account_address,
            "gas": 200000,
            "gasPrice": w3.to_wei("500", "gwei"),
            "nonce": w3.eth.get_transaction_count(account_address),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)

def main():
    MQTT_ADDRESS = "192.168.1.80"
    MQTT_USER = "mosq"
    MQTT_PASSWORD = "Jordan@2020"
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_ADDRESS, 1883)
    # mqtt_client.loop_forever()
    
if __name__ == "__main__":
    print("MQTT to InfluxDB bridge")
    main()
