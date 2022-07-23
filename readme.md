# zz

一个简陋的不能再简陋的聊天程序

## sever

#### 如何处理客户端请求
服务器将从客户端接收请求，并将字符串转换为列表
```
conn, u_host = s.accept()
request = conn.recv(1024).decode()
massages = request.split(",")
```
根据第一个数字确定消息请求的服务

+ massages = [0, user_name, password, ip]
   
    处理注册请求,为用户分配一个5位唯一ZZ ID号码
    
    将zz_id, user_name, password, ip 记录在服务器
  
    将用户状态设为 1 (在线)

    返回[0, zz_id]


+ massages = [1, zz_id, password, ip]
   
  处理登录请求, 查找zz_id并验证password
  
  入果登陆成功就记录下IP地址,并将状态设为 1 (在线)

  成功返回[0]

  密码错误返回[1]

  id不存在返回[2]


+ massages = [2, zz_id]

  处理好友请求,返回好友列表

  返回[friend_1, friend_2, ... ]

  如无则返回[]


