
name=input('Enter Name: ')                                                                                                                  

print()

o=int(input('1.Server\n2.Client\nEnter Choice: '))

print()

host=''

if o==1:

    port=input('Enter port no. (for default=9999 press Enter): ')
    
    if not port:
        port=9999 
    else: 
        port=int(port)

elif o==2:    

    link=input('Enter connection link ( Press Enter for other method) : ')

    if not link:
        host=input('Enter host (for default=localhost press Enter): ')
        port=input('Enter port no. (for default=9999 press Enter): ')
        if not host:
            host='localhost'
        if not port:
            port=9999
        else:
            port=int(port)
    else:
        hp=link.split('//')[1]
        host=hp.split(':')[0]
        port=int(hp.split(':')[1])
    
    print()

else:    
    print('Enter valid choice.')
    exit()
