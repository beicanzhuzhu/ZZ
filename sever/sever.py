# zz sever-side
import random
import socket
import json


class Sever:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @property
    def __zz_id(self):

        # 生成新zz_id
        __id = []

        for i in range(0, 5):
            __id[i] = random.randint(1, 9)
        return __id

    def wait_handle_request(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        s.listen(3)

        conn, u_host = s.accept()
        request = conn.recv(1024).decode()

        print("来自 ", u_host, " 的链接 : [", request, "]")

        massages = request.split(",")

        if massages[0] == "0":
            id = str(self.__zz_id)

            with open("users.json", "r") as u:
                a = json.load(u)


