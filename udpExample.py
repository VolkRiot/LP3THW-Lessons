import socket

target_host = '127.0.0.1'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'.encode(),
              (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)
