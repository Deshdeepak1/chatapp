from chatapp import o,host,port,name
from .server import server
from .client import client    

if __name__=='__main__':
    if o==1:
        server(port,name)
    elif o==2:
        client(host,port,name)
