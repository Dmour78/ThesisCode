import ipfshttpclient
import time

# Connect to the local IPFS node
ipfs = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

def measure_latency(fn, prompt):
    file_name = input(prompt)
    start_time = time.time()
    fn(file_name)
    end_time = time.time()
    latency = end_time - start_time
    print(f"Latency: {latency} seconds\n")

def measure_write_latency(file_name):
    with open(file_name, 'rb') as file:
        file_content = file.read()
        ipfs.add_bytes(file_content)

def measure_read_latency(file_name):
    cid = ipfs.add(file_name)['Hash']
    ipfs.get(cid)

def measure_upload_time(file_name):
    with open(file_name, 'rb') as file:
        file_content = file.read()
        start_time = time.time()
        ipfs.add_bytes(file_content)
        end_time = time.time()
        upload_time = end_time - start_time
        print(f"Upload time: {upload_time} seconds\n")

def measure_ftp_performance(file_name):
    # Placeholder for FTP performance measurement
    # Replace this with your FTP logic (upload or download)
    print("Performing FTP operation (placeholder)")

if __name__ == "__main__":
    while True:
        print("Choose Measurement:")
        print("1. Measure Write Latency")
        print("2. Measure Read Latency")
        print("3. Measure Upload Time")
        print("4. Measure FTP Performance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            measure_latency(measure_write_latency, "Enter file name for write latency measurement: ")
        elif choice == '2':
            measure_latency(measure_read_latency, "Enter file name for read latency measurement: ")
        elif choice == '3':
            measure_latency(measure_upload_time, "Enter file name for upload time measurement: ")
        elif choice == '4':
            measure_latency(measure_ftp_performance, "Enter file name for FTP performance measurement: ")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
