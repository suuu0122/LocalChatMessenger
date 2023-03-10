from faker import Faker
import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"Starting up on {server_address}")
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    
    try:
        print(f"connection from {client_address}")
        while True:
            data = connection.recv(16)
            data_str = data.decode("utf-8")
            print(f"Received {data_str}")
            if data:
                fake = Faker()
                fake_text = fake.text()
                connection.sendall(fake_text.encode("utf-8"))
            else:
                print(f"no data from {client_address}")
                break
    finally:
        print("Closing current connection")
        connection.close()