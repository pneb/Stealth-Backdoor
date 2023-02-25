import socket

class Shell:
    def __init__(self, server_ip, server_port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((server_ip, server_port))

    def send_command(self, command):
        self.connection.send(command.encode())
        return self.connection.recv(1024).decode()

def execute_command(command, server_ip, server_port):
    shell = Shell(server_ip, server_port)
    return shell.send_command(command)
