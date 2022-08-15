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

    @staticmethod
    def _process_the_input(string):
        # 剔除字符串中所有的空格
        string = ''.join([i for i in string if i != " "])
        # 经过如下处理后，合法输入的第一项会是''
        string = string.split("-")
        # 如果不是，则输入非法
        if string[0] != '':
            return None
        string.pop(0)
        return string

    def _receive(self):

        request = self._s.recv(1024).decode()
        if not request:
            self._error(0)

        massages = request.split(",")

        pass

    def _get_input(self):
        pass

    def _error(self, error_code):
        pass

    def start(self):

        print("Welcome to use zz.")
        print("Enter -s <zz_id> -p <password> to sign in "
              "or -r  <name> -p <password> to register")
        while True:
            print("zz(" + self._information["name"] + ")->", end="")

            command = input()
            command = self._process_the_input(command)
            if command is None:
                self._error(1)
            else:
                break

        if command[0][0] == "s":
            pass
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
