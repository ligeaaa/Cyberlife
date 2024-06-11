import os
import socket
import threading

from common.msg import Message
from constants.msg_type_constants import BORN, DEATH


def check_port_occupied(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
    except OSError as e:
        return True  # 端口被占用
    return False  # 端口未被占用

def kill_process_using_port(port):
    cmd = f"netstat -ano | findstr :{port}"
    result = os.popen(cmd).read()
    if result:
        pid = result.strip().split()[-1]
        os.system(f"taskkill /f /pid {pid}")
        print(f"Process using port {port} has been killed.")

class Server_Data:
    born_count = 0
    death_count = 0

    def process(self, msg: bytes):
        msg = Message.decode(msg)
        kind = msg.kind
        if kind == BORN:
            count = msg.information["count"]
            self.born_count += count
        if kind == DEATH:
            count = msg.information["count"]
            self.death_count += count

    def __str__(self):
        return f"Born: {self.born_count}\nDeath: {self.death_count}"


class Server:
    def __init__(self, host='localhost', port=65432):
        if check_port_occupied(port):
            kill_process_using_port(port)

        self.data_storage = Server_Data()
        self.server_address = (host, port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(1)
        print(f'Server is listening on {self.server_address}')

    def start(self):
        while True:
            connection, client_address = self.server_socket.accept()
            a = threading.Thread(target=self.handle_client, args=(connection,))
            a.start()

    def handle_client(self, connection):
        print(1)
        try:
            while True:
                msg = connection.recv(1024)
                if msg:
                    self.data_storage.process(msg)
                else:
                    break
        except Exception as e:
            print(e)