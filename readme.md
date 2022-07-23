# zz

A little chat program

## sever

#### About how to handle the massages
服务器将从客户端接收消息，并将字符串转换为列表
```
conn, u_host = s.accept()
request = conn.recv(1024).decode()
massages = request.split(",")
```
根据第一个数字确定消息请求的服务

+ massages = [0, user_name, password, ip]
   
    处理注册请求,为用户分配一个5位唯一ZZ ID号码
    
    将zz_id, user_name, password, ip 记录在服务器

    返回[0, zz_id]