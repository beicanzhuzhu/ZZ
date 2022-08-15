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
        a = 6
        while a != 0:
            print("Please enter your zz_id:", end="")
            zz_id = input()
            print("Please enter your password:", end="")
            password = input()
            self._s.send(",".join([1, zz_id, password]).encode())
            if self._s.recv(1024).decode().split(",")[0] == "1":
                a -= 1
                print("Password error, please try again.")
                print("(You have " + str(a) + " times.)")
            elif self._s.recv(1024).decode().split(",")[0] == "2":
                print("Can't find the user " + zz_id + ", please try again.")

        if a == 0:
            print("Too many password errors!!")






        print("""
Welcome to zz!
'-p' to change the sever ip.
'-t <your friend's name or zz_id>' to chat with your friend  
Or you can input '-h' to get more help.
                    """)

        while True:
            print("zz(" + self._information["name"] + ")->", end="")
            common = input()


if __name__ == "__main__":

    user = User(socket.gethostbyname("56gm316515.goho.co"), 55439)
    user.start()
