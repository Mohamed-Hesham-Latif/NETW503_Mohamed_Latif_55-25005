import socket
import select
import sys
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=50008
client_socket.connect(('127.0.0.1',port))
while True:
    message = input("Enter your message: ")
    message_bytes = message.encode('utf-8')
    client_socket.send(message_bytes)


    response_bytes = client_socket.recv(1024)
    decoded_client=response_bytes.decode('utf-8')
    print(decoded_client)

    if message == "CLOSE SOCKET":
        client_socket.close()
        break
