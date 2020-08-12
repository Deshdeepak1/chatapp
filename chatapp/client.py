import socket

def client(host,port,name):

    c=socket.socket()
    try:
        c.connect((host,port))
    except socket.error as e:
        print(e)
        exit()

    c.send(bytes(name,'utf-8'))
    other=c.recv(1024).decode()
    print('Chatting with: '+other)
    print()

    while True:
        print(other+' : ',c.recv(1024).decode())
        msg=input(name+' : ')
        c.send(bytes(msg,'utf-8'))
