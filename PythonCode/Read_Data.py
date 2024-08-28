""" import time
import ftplib

# Get file name from user input
file_name = input("Enter the file name: ")

# Connect to the FTP server
ftp = ftplib.FTP('127.0.0.1')  # Replace with the hostname or IP of the FTP container
ftp.login('yourName', 'yourPass')  # Replace with the FTP credentials

# Start measuring time
start_time = time.time()

# Retrieve the file
try:
   ftp.retrbinary(f"RETR {file_name}", open(file_name, 'wb').write)
except ftplib.all_errors as e:
   print("FTP error:", e)
   exit()

# End time measurement
end_time = time.time()

# Calculate latency
latency_seconds = end_time - start_time

# Print the result
print(f"Read latency for file '{file_name}': {latency_seconds:.4f} seconds")

# Close the FTP connection
ftp.quit() """


import time
import ftplib
import resource

# Get file name from user input
file_name = input("Enter the file name: ")

# Connect to the FTP server
ftp = ftplib.FTP('127.0.0.1')  # Replace with the hostname or IP of the FTP container
ftp.login('yourName', 'yourPass')  # Replace with the FTP credentials

# ===== Write latency measurement =====

# Start measuring time and CPU time
start_write_time = time.time()
start_write_cpu_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime

# Send the file
try:
    with open(file_name, 'rb') as f:
        ftp.storbinary(f"STOR {file_name}", f)
except ftplib.all_errors as e:
    print("FTP error during writing:", e)
    exit()

# End time and CPU time measurement
end_write_time = time.time()
end_write_cpu_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime

# Calculate write latency and CPU writing time
write_latency_seconds = end_write_time - start_write_time
cpu_writing_time = end_write_cpu_time - start_write_cpu_time

# ===== Read latency measurement =====

# Start measuring time and CPU time
start_read_time = time.time()
start_read_cpu_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime

# Retrieve the file
try:
    ftp.retrbinary(f"RETR {file_name}", open(file_name, 'wb').write)
except ftplib.all_errors as e:
    print("FTP error during reading:", e)
    exit()

# End time and CPU time measurement
end_read_time = time.time()
end_read_cpu_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime

# Calculate read latency and CPU reading time
read_latency_seconds = end_read_time - start_read_time
cpu_reading_time = end_read_cpu_time - start_read_cpu_time

# Print the results
print(f"Write latency for file '{file_name}': {write_latency_seconds:.4f} seconds")
print(f"CPU time for writing: {cpu_writing_time:.4f} seconds")
print(f"Read latency for file '{file_name}': {read_latency_seconds:.4f} seconds")
print(f"CPU time for reading: {cpu_reading_time:.4f} seconds")

# Close the FTP connection
ftp.quit()