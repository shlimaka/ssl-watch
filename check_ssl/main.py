import os
import ssl


print(os.environ['SSLWATCH_CONFIG_DIR'])

print(os.listdir(os.environ['SSLWATCH_CONFIG_DIR']))
print("xuy")

# print(ssl.get_server_certificate(('vm-harbor-01.ipa.dev.sigmaukraine.com',443)))



from datetime import datetime
import OpenSSL
# import ssl
cert=ssl.get_server_certificate(('vm-harbor-01.ipa.dev.sigmaukraine.com', 443))
print(cert)
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
print("---------------")

print(x509)
print("---------------")
bytes=x509.get_notAfter()
print("---------------")

print(bytes)
print("---------------")

timestamp = bytes.decode('utf-8')
print (datetime.strptime(timestamp, '%Y%m%d%H%M%S%z').date().isoformat())