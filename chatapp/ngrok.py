import os

try:
    import requests
except:
    os.system('pip3 install requests')
    import requests

from time import sleep

HOME=os.environ.get('HOME')

def Ngrok(port,authtoken):

    print()

    if HOME=='/data/data/com.termux/files/home':

        if authtoken=='':
            pass
        else:
            os.system('./ngrok authtoken '+authtoken)
        os.system('./ngrok tcp '+str(port)+' > /dev/null &')
        sleep(10)
        res=requests.get('http://127.0.0.1:4040/api/tunnels')
        false=0
        link=eval(res.__dict__['_content'].decode())["tunnels"][0]['public_url']
        print("Connection link : "+link)

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
