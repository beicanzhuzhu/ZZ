# user_side

import socket
import json
import threading


class User:

    def __init__(self, host, port):
        self._s = socket.socket()
        self._s.connect((host, port))

    def log_in(self):
        pass

    def register(self):
        pass


