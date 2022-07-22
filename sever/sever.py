# zz sever-side

import socket


class Sever:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def wait_handle_request(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        s.listen(3)

        conn, u_host = s.accept()
        request = conn.recv(1024).decode()

        print("来自 ", u_host, " 的链接 : [", request, "]")

        massages = request.split(",")
