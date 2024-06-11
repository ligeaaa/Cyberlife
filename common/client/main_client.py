import socket

from common.msg import Message


class Client:
    def __init__(self, host='localhost', port=65432):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.client_socket.connect(self.server_address)
        self.client_socket.settimeout(5)  # Set timeout for 5 seconds

    def send_information(self, msg: Message):
        try:
            self.client_socket.sendall(msg.encode())
        except Exception as e:
            print(f"An error occurred: {e}")

    def close(self):
        self.client_socket.close()
