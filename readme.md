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

+ massges = [1, zz_id, password, ip]
   
  处理登录请求, 查找zz_id并验证password
  
  入果登陆成功就记录下IP地址,并将状态设为 1 (在线)