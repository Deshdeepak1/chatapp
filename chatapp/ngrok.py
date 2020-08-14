import os
from time import sleep


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
        os.system('pip3 install pyngrok')
        print()

        from pyngrok import ngrok

        if authtoken=='':
            pass
        else:
            ngrok.set_auth_token(authtoken)
        link=ngrok.connect(port,'tcp')
        print("Connection link : "+link)
