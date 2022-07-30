# user_side

import socket
import json
import threading


class User:

    def __init__(self, host, port):
        self._s = socket.socket()
        self._s.connect((host, port))
        self._information = {"name": "", "zz_id": "",
                             "friends": [], "friend_request": [],
                             }

    def _show_friends(self):
        pass

    def _show_friend_request(self):
        pass

    def _show_chat_interface(self):
        pass

    def _receive(self):

        request = self._s.recv(1024).decode()
        if not request:
            self._error(0)

        massages = request.split(",")

        pass

    def _input(self):
        pass

    def _get_input(self):
        pass

    def _error(self, error_code):
        pass

    def start(self):

        while True:
            print("""
            welcome to ZZ!!
            -------------------
            1.聊天记录
            2.
                  """)


if __name__ == "__main__":

    user = User(socket.gethostbyname("56gm316515.goho.co"), 55439)
    user.start()
