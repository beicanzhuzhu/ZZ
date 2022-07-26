# zz sever-side

from random import randint
import socket
import pymysql
import threading


class Sever:

    def __init__(self, host, port, m_user, m_password, m_host="localhost", m_port=0):
        """
        初始化zz服务器

        :param host: 服务器地址
        :param port: 服务器监听端口
        :param m_user: mysql服务器用户
        :param m_password: MySQL用户密码
        :param m_host: MySQL服务器地址, 默认为localhost
        :param m_port: MySQL服务器端口, 默认为3306
        """

        # 初始化服务器
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind((host, port))
        self._s.listen(5)
        # 连接列表 [{"zz_id": zz_id, "conn": conn}, ...]
        self._conns = []
        # 代办列表 [{"zz_id": zz_id, "matter": [...]}, ...]
        self._to_do_list = []

        # 连接数据库
        try:
            self._db = pymysql.connect(user=m_user, password=m_password, host=m_host, port=m_port, database="zz")
        # zz数据库不存在
        except pymysql.err.OperationalError:

            try:
                self._db = pymysql.connect(user=m_user, password=m_password, host=m_host, port=m_port)
            # 连接不到服务器
            except pymysql.err.OperationalError:
                raise pymysql.err.OperationalError("无法连接到MYSQL服务器,请检查服务器是否打开或依据https://github.com/beicanzhuzhu/ZZ"
                                                   "配置MYSQL服务器。")
            self._database = self._db.cursor()
            self._database.execute("create database zz")
            self._db.close()
            self._db = pymysql.connect(user=m_user, password=m_password, host=m_host, port=m_port, database="zz")
            self._database = self._db.cursor()
            # 创建数据表
            sql = """
            create table users(
            zz_id     int(5) primary key ,
            name      varchar(25),
            first_login_time datetime,
            last_login_time  datetime,
            is_online        bit(1),
            friends          text
            );"""
            self._db.commit()
            self._database.execute(sql)
            # 插入root管理员的账户
            sql = """
            insert into zz.users (zz_id, name, first_login_time, last_login_time, is_online, friends)
            value 
            (00001, 'root', NOW(), NOW(), 1, '');"""
            self._database.execute(sql)
            self._db.commit()

        else:
            self._database = self._db.cursor()

        print("working...")

    @property
    def _zz_id(self):  # 还需修改，防止重复
        # 生成新zz_id
        return randint(10000, 99999)

    def _send_massage(self, zz_id_1, zz_id_2, massage):
        """
        发送消息,对方不在线则加入代办列表

        :param zz_id_1: 发送用户的zz_id
        :param zz_id_2: 被发送用户的zz_id
        :param massage: 发送的消息
        :return: None
        """
        # 查询是否在线
        for i in self._conns:
            if i["zz_id"] == zz_id_2:  # 在线
                i["conn"].send(",".join(["0", zz_id_1, massage]).encode())
        self._to_do_list.append({"zz_id": zz_id_1, "matter": [0, zz_id_1, zz_id_2, massage]})

    def _send_friend_request(self, zz_id_1, name, zz_id_2):
        """
        发送好友申请请求,不在线则加入代办列表

        :param zz_id_1: 请求用户的zz_id
        :param name: 请求用户的昵称
        :param zz_id_2: 被请求用户的zz_id
        :return: None
        """
        # 查询是否在线
        for i in self._conns:
            if i["zz_id"] == zz_id_2:  # 在线
                i["conn"].send(",".join(["1", zz_id_1, name]).encode())
        self._to_do_list.append({"zz_id": zz_id_1, "matter": [0, zz_id_1, name, zz_id_2]})

    def _handle_request(self, conn, port):
        """
        处理用户端发送的消息

        :param conn: 对应用户连接实例
        :param port: 对应用户地址
        :return: None
        """
        print(port, "已连接")

        while True:
            # 接收用户端消息
            request = conn.recv(1024).decode()
            # 如果消息为空，用户下线
            if not request:
                print(port, "已断开连接")
                # 将用户状态设为 0 (下线)
                break
            # 打印有关消息
            print("来自 ", port, " 的消息 : [", request, "]")
            # 将消息分割为列表
            massages = request.split(",")

            # 开始处理消息

            # 先将用户加入连接列表
            if massages[0] != 0 and {"zz_id": massages[1], "conn": conn} not in self._conns:
                self._conns.append({"zz_id": massages[1], "conn": conn})

            # 注册
            # [0, user_name, password]
            if massages[0] == "0":
                zz_id = str(self._zz_id)
                #
                # 将用户加入连接列表
                self._conns.append({"zz_id": massages[1], "conn": conn})

            # 登陆
            # [1, zz_id, password]
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

            # 删除好友好友
            # [4, zz_id_1, zz_id_2]
            elif massages[0] == "4":
                pass

    def start(self):
        """
        开始启服务器

        :return: None
        """
        while True:
            # 等待连接
            conn, port = self._s.accept()
            # 接收连接并分配线程处理
            thread = threading.Thread(target=self._handle_request, args=(conn, port))
            # 守护线程
            thread.daemon = True
            thread.start()


if __name__ == '__main__':
    sever = Sever("", 8080, "beicanyuzhuzhu", "070212", "192.168.31.160")
    sever.start()
