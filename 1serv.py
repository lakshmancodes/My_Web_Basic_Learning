import socket
s=socket.socket()
port=8000
s.bind(('localhost',port))
s.listen(5)
while True:
    c,address=s.accept()
    print('Successful',address)
    data={"LAKSHMAN":"123","PRAVEEN":"123","SHIVA":"111"}
    msg=c.recv(1024)
    x=msg.split(" ")
    u_name=x[0]
    psw=x[1]
    flag=0
    for key,value in data.items():
        if key==u_name and value==psw:
            flag=1
        elif(key==u_name and value!=psw):
            c.send("Wrong password")
        else:
            continue
    if flag==1:
        c.send("Welcome user!")
    else:
        c.send("Invalid login")
    c.close()