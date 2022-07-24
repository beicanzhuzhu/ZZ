# zz sever-side
import random
import socket
import json
import threading


class Sever:

    def __init__(self, host, port):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)

    @property
    def __zz_id(self):

        # 生成新zz_id
        __id = []

        for i in range(0, 5):
            __id[i] = random.randint(1, 9)

        return __id

    def handle_request(self, conn, port):

        while True:

            request = conn.recv(1024).decode()

            print("来自 ", port, " 的链接 : [", request, "]")

            massages = request.split(",")

            if massages[0] == "0":

                id = str(self.__zz_id)

                with open("users.json", "r") as u:
                    a = json.load(u)

    def wait_handle_request(self):

        while True:
            conn, port = self.s.accept()

            thread = threading.Thread(target=self.handle_request, args=(conn, port))
            thread.setDaemon(True)
            thread.start()
