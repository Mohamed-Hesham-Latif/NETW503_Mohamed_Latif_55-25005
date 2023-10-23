import socket
import threading
PORT = 50008
ADDR = ('127.0.0.1', PORT)
def threaded(conn, addr):
    client_socket = conn
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if "CLOSE SOCKET" in message:
            break
        capitalized_message = message.upper()
        client_socket.send(capitalized_message.encode('utf-8'))
    client_socket.close()
def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        print("[NEW CONNECTION] " + str(addr) + " connected.")
        threading.Thread(target=threaded, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
if __name__ == "__main__":
    main()