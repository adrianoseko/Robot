import os

# Testando conexão
def ping(hostname):
    response = os.system("ping -c 1 " + hostname)

    if response == 0:

        print(hostname, 'is up!')
        return(1)
    else:
        print( hostname, 'is down!')
        return(0)

