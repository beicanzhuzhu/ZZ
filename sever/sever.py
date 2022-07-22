# zz sever-side

import socket

class Sever:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def wait_request(self, massage):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        s.listen(3)
