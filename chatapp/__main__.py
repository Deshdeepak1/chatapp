import socket
import os
from time import sleep
from pyngrok import ngrok
from chatapp import o,host,port,name

def Ngrok(port,authtoken):

    print()
     
    if os.environ['HOME']=='/data/data/com.termux/files/home':
        
        if authtoken=='':
            pass
        else:
            os.system('./ngrok authtoken '+authtoken)
        os.system('./ngrok tcp '+str(port)+' > /dev/null &')
        sleep(10)
        os.system('link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "tcp://[0-9a-z]*.tcp.ngrok.io:[0-9]*") && echo "Connection link ": $link')

    else:
        if authtoken=='':
            pass
        else:
            ngrok.set_auth_token(authtoken)
        link=ngrok.connect(port,'tcp')
        print("Connection link : "+link)
    


def server(port,name):
    
    s=socket.socket()
    
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
        Ngrok(port,authtoken)

    print()

    while True:
        c,addr=s.accept()
        c.send(bytes(name,'utf-8'))
        other=c.recv(1024).decode()
        print('Chatting with: '+other)
        print()

        while True:
            msg=input(name+' : ')
            c.send(bytes(msg,'utf-8'))
            print(other+' : ',c.recv(1024).decode())


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

if o==1:
    server(port,name)
elif o==2:
    client(host,port,name)
