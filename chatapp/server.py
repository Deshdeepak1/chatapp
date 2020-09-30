from .ngrok import Ngrok
import socket


def server(port,name):

    s=socket.socket()

    try:
        s.bind(('',port))
    except socket.error as e:
        print(e)
        exit()

    s.listen(1)

    ng=input("Enter 1 for ngrok (Press Enter to not use ngrok.) : ")

    if not ng:
        print('Starting without ngrok.')
    elif int(ng)==1:
        authtoken=input('Enter authtoken (Press Enter to not change.) : ')
        link=Ngrok(port,authtoken)
        print("Connection link:",link)

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
