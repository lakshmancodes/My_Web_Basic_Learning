import socket
c=socket.socket()
port=8000
c.connect(('localhost',port))
u_name=raw_input("Enter your username: ")
psw=raw_input("Enter your password: ")
c.send(u_name)
c.send(" ")
c.send(psw)
if(c.recv(1024)=="Welcome user!"):
    print 'Welcome ',u_name
c.close()