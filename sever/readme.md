# zz

一个简陋的不能再简陋的聊天程序

## sever.py

#### 处理多个用户

每接入一个连接就新开一个线程处理，然后等待新的连接
```
while True:
    conn, port = self.s.accept()
    thread = threading.Thread(target=self.__handle_request, args=(conn, port))
    thread.setDaemon(True)
    thread.start()
```

#### 处理下线

如果接收消息为空(false) 将用户状态设为 0 (下线) 结束线程
```
request = conn.recv(1024).decode()
if not request:
    print(port, "已断开连接")
    # 将用户状态设为 0 (下线)
    break
```

#### 处理用户端请求
服务器将从用户端接收请求，并将字符串转换为列表
```
request = conn.recv(1024).decode()
massages = request.split(",")
```
根据第一个数字确定消息请求的服务

+ massages = [0, user_name, password]
   
    注册  
    为用户分配一个5位唯一ZZ ID号码  
    将zz_id, user_name, password记录在服务器  
    将用户状态设为 1 (在线)  
    返回[0, zz_id]

+ massages = [1, zz_id, password]
   
    登录  
    查找zz_id并验证password  
    入果登陆成功将状态设为 1 (在线)  
    成功返回[0]  
    密码错误返回[1]  
    id不存在返回[2]
  
+ massages = [2, zz_id_1, zz_id_2]
  
    添加好友  
    zz_id_2 存在就向指定用户[发送好友请求](#1)并返回[1]  
    zz_id_2 不存在就返回[0]
  


+ massages = [3, zz_id]

    处理好友请求,返回好友列表  
    返回[friend_1, friend_2, ... ]  
    如无则返回[]

#### <a id="1" >发送好友请求</a>
