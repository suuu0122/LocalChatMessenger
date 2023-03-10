import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "socket_file"
print(f"connecting to {server_address}")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        message = input()
        encode_message = message.encode("utf-8")
        sock.sendall(encode_message)
            
        data = sock.recv(32).decode("utf-8")
        if data:
            print(f"Server response: {data}")
        else:
            break
finally:
    print("closing socket")
    sock.close()