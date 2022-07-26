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

    def _show_main_window(self):
        pass

    def _show_friends(self):
        pass

    def _show_friend_request(self):
        pass

    def _show_chat_interface(self):
        pass

    def receive(self):
        pass

    def log_in(self):
        pass

    def register(self):
        pass


if __name__ == "__main__":
    pass
