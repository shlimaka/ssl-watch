import os
import ssl
import datetime
import socket
SSLWATCH_CONFIG_DIR=os.environ['SSLWATCH_CONFIG_DIR']
# print(os.environ['SSLWATCH_CONFIG_DIR'])

conf_files = [f for f in os.listdir(SSLWATCH_CONFIG_DIR) if f.endswith(".conf")]

file_path = SSLWATCH_CONFIG_DIR + conf_files[1]  # Replace with your file's path

# Initialize an empty variable to store the file contents
file_contents = ""

# Open the file for reading
try:
    with open(file_path, "r") as file:
        # Read the contents of the file
        file_contents = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Now, the variable file_contents contains the content of the file
print(file_contents)

hostname = 'ssus-stage.i.sigmaukraine.com'
port = 443  # Default HTTPS port

# Create a socket and wrap it with an SSL context
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = (ssock.getpeercert())

expiration_date_str = cert["notAfter"]
# print (expiration_date_str)

file_path = "/tmp/ssl-watch/test.txt"  # Replace with the desired file path

# Data to write to the file
data_to_write = expiration_date_str

# Open the file for writing (create the file if it doesn't exist)
with open(file_path, "w") as file:
    # Write the data to the file
    file.write(data_to_write)

# The file is automatically closed when the 'with' block is exited
print("Data has been written to the file.")


import server 