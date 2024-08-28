import time
import requests
from web3 import Web3

# Connect to Ethereum network using Geth
w3 = Web3(Web3.HTTPProvider('http://172.28.96.1:7545'))

def calculate_latency(transaction_hashes):
    latencies = []
    for transaction_hash in transaction_hashes:
        # Start the timer
        start_time = time.time()

        # Check if the transaction has been confirmed
        while not w3.eth.get_transaction_receipt(transaction_hash):
            time.sleep(1)

        # Stop the timer
        end_time = time.time()

        # Calculate latency
        latency = end_time - start_time
        latencies.append(latency)

    return latencies

def calculate_throughput(transaction_hashes, duration):
    total_transactions = len(transaction_hashes)
    throughput = total_transactions / duration

    return throughput

# Send transactions
transaction_hashes = []
for i in range(100):
    transaction_hash = w3.eth.send_transaction({
        'from': w3.eth.accounts[1],
        'to': w3.eth.accounts[0],
        'value': 1000000000000
    })

    transaction_hashes.append(transaction_hash)

# Calculate latency
latencies = calculate_latency(transaction_hashes)

# Calculate throughput
duration = 60 # Duration in seconds
throughput = calculate_throughput(transaction_hashes, duration)

print("Average latency:", sum(latencies) / len(latencies))
print("Throughput:", throughput)
