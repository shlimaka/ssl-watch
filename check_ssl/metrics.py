from datetime import datetime
import OpenSSL
import ssl

domain="example.com"

def date():
    print(domain)


date()

# cert=ssl.get_server_certificate(('www.yahoo.com', 443))
# x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
# bytes=x509.get_notAfter()
# print(bytes)
# timestamp = bytes.decode('utf-8')
# print (datetime.strptime(timestamp, '%Y%m%d%H%M%S%z').date().isoformat())


# with open('output.txt', 'a') as f:
#     f.write('asd')

# file_path = 'output.txt'

# with open(file_path, 'r') as file:
#     for line in file:
#         print(line, end='')

