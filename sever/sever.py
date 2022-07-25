# zz sever-side
import random
import socket
import json
import threading


class Sever:

    def __init__(self, host, port):

        # 初始化服务器
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)
        self.__conns = []

    @property
    def __zz_id(self):  # 还需修改，防止重复

        # 生成新zz_id
        __id = []

        for i in range(0, 5):
            __id[i] = random.randint(1, 9)

        return __id

    def __handle_request(self, conn, port):

        while True:
            # 接收用户端消息
            request = conn.recv(1024).decode()
            # 如果消息为空，用户下线
            if not request:
                print(port, "已断开连接")
                # 将用户状态设为 0 (下线)
                break
            # 打印有关消息
            print("来自 ", port, " 的链接 : [", request, "]")
            # 将消息分割为列表
            massages = request.split(",")
            
            # 开始处理消息

            # 先将用户加入连接列表
            if massages[0] != 0 and {"zz_id": massages[1], "conn": conn} not in self.__conns:
                self.__conns.append({"zz_id": massages[1], "conn": conn})

            # 注册
            # [0, user_name, password, ip]
            if massages[0] == "0":
                zz_id = str(self.__zz_id)
                with open("users.json", "r") as u:
                    a = json.load(u)
                    a.append({"name": massages[1], "zz_id": zz_id, "password": massages[2]})
                # 将用户加入连接列表
                self.__conns.append({"zz_id": massages[1], "conn": conn})
                    
            # 登陆
            # [1, zz_id, password, ip]
            elif massages[0] == "1":
                pass
            
            # 添加好友
            # [2, zz_id_1, zz_id_2]
            elif massages[0] == "2":
                pass
            
            # 获取好友列表
            # [3, zz_id]
            elif massages[0] == "3":
                pass

    def start(self):

        while True:
            # 等待连接
            conn, port = self.s.accept()
            # 接收连接并分配线程处理
            thread = threading.Thread(target=self.__handle_request, args=(conn, port))
            # 守护线程
            thread.daemon = True
            thread.start()
