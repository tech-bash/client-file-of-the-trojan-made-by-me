import socket
c=socket.socket()
ip='192.168.150.128'
c.connect((ip,9999))
data =c.recv(2014).decode()
print(data);
data2 =c.recv(2014).decode()

if data2=="input" :
       x=input("enter the command")
       c.send(bytes(x,'utf-8'))
       data3 = c.recv(2014).decode()
       print(str(data3))