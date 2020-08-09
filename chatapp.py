import socket
import os
from time import sleep


def ngrok(port,authtoken):
    
    HOME= os.environ['HOME']

    if authtoken=='':
        pass
    else:
        with open(HOME+'/.ngrok2/ngrok.yml','w') as f:
            f.write('authtoken: '+authtoken)

    
    os.system('./ngrok tcp '+str(port)+' > /dev/null &')
    sleep(10)
    os.system('link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "tcp://[0-9a-z]*.tcp.ngrok.io:[0-9]*") && echo "Connection link tcp://host:port " : $link')


def server():
    name=input('Enter Name: ')
    s=socket.socket()
    port=input('Enter port no. (for default=9999 press Enter): ')
    if port=='':
        port=9999
    else:
        port=int(port)
    try:
        s.bind(('',port))
    except socket.error as e:
        print(e)
        exit()
    s.listen(1)
    
    ng=input("Enter 1 for ngrok (Press Enter to not use ngrok.) : ")
    
    if ng=='':
        print('Starting without ngrok.')
    elif int(ng)==1:
        authtoken=input('Enter authtoken (Press Enter to not change.) : ')
        ngrok(port,authtoken)

    while True:
        c,addr=s.accept()
        c.send(bytes(name,'utf-8'))
        print('Chatting with: ',c.recv(1024).decode())
        while True:
            msg=input('Send message: ')
            c.send(bytes(msg,'utf-8'))
            print('Recieved message: ',c.recv(1024).decode())


def client():
    name=input('Enter Name: ')
    c=socket.socket()
    
    link=input('Enter connection link ( Press Enter for other method) : ')
    
    if link=='':
        host=input('Enter host (for default=localhost press Enter): ')
        port=input('Enter port no. (for default=9999 press Enter): ')
        if host=='':
            host='localhost'
        if port=='':
            port=9999
        else:
            port=int(port)
    else:
        hp=link.split('//')[1]
        host=hp.split(':')[0]
        port=int(hp.split(':')[1])

    try:
        c.connect((host,port))
    except socket.error as e:
        print(e)
        exit()
    
    c.send(bytes(name,'utf-8'))
    print('Chatting with: ',c.recv(1024).decode())
    
    while True:
        print('Recieved message: ',c.recv(1024).decode())
        msg=input('Send message: ')
        c.send(bytes(msg,'utf-8'))


o=int(input('1.Server\n2.Client\nEnter Choice: '))


if o==1:
    server()
elif o==2:
    client()
else:
    print('Enter valid choice.')
