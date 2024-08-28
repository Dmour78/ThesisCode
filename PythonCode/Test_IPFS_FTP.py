from ftplib import FTP, error_perm
import time
import os
import socket
import logging
import subprocess


logging.basicConfig(level=logging.INFO)

def measure_latency_read(host, user, password, filename):
    with FTP() as ftp:
        try:
            ftp.connect(host, 21, timeout=5)
            ftp.login(user, password)
            ftp.set_pasv(True)  # Set passive mode
            start_time = time.time()
            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR ' + os.path.basename(filename), file.write)
            end_time = time.time()
            logging.info(f"Read latency: {end_time - start_time} seconds")
        except error_perm as err:
            logging.error('Read operation error: %s', err)
        except Exception as err:
            logging.error('An unexpected error occurred during the read operation: %s', err)

def measure_latency_write(host, user, password, local_file_path):
    with FTP() as ftp:
        try:
            print(host)
            ftp.connect(host, 21, timeout=10)
            ftp.login(user, password)
            ftp.set_pasv(True)  # Set passive mode
            start_time = time.time()
            with open(local_file_path, 'rb') as file:
                ftp.storbinary('STOR ' + os.path.basename(local_file_path), file)
            end_time = time.time()
            logging.info(f"Write latency: {end_time - start_time} seconds")
        except error_perm as err:
            logging.error('Write operation error: %s', err)
        except Exception as err:
            logging.error('An unexpected error occurred during the write operation: %s', err)

def main():

# Discover the container IP address using Docker inspect
    #ftp_host = subprocess.check_output(["docker", "inspect", "--format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", "34246b803b09af64a8c1b2de95705336fccfc7c4e078b9398a28f173c42c5642"]).decode().strip("'")

    # Get the IP address of the vsftpd container
    ftp_host = '127.0.0.1'
    
    #ftp_host = socket.gethostbyname(socket.gethostname())
    ftp_user = 'yourName'
    ftp_password = 'yourPass'
    test_file = 'Ipfs1KB.txt'

    try:
        file_path = input('Enter the local path of the text file to upload: ')
        measure_latency_write(ftp_host, ftp_user, ftp_password, file_path)

        measure_latency_read(ftp_host, ftp_user, ftp_password, test_file)
    except KeyboardInterrupt:
        logging.warning('User interrupted the program.')
    except Exception as e:
        logging.error('An unexpected error occurred: %s', e)

if __name__ == "__main__":
    main()
