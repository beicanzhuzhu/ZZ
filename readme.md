#zz

A little chat program

###About how to handle the massages
The server will receive the message from the client and convert the string into a list
```
conn, u_host = s.accept()
request = conn.recv(1024).decode()
massages = request.split(",")
```
Determine the service requested by the message according to the first number

+[1,]