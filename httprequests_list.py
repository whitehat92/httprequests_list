import requests
import sys

# I need a host and then append the list from command line

#list can only contain some word or an "/" after the word
ler = open(sys.argv[1], 'r')
#printavel = ler.read()
#host = "https://app.pipedrive.com/"
#print(printavel)
#print (printavel.split()[4])


for url in ler:
    site = "https://app.pipedrive.com/"
    sendHTTPS = requests.get(site + str(url))
    pedidoHTTPS = sendHTTPS.status_code
    cabecaHTTPS = sendHTTPS.headers
    pedido = sendHTTPS.status_code
    cabeca = sendHTTPS.headers
    print (site + str(url) + "\n" + str(pedidoHTTPS))
    print (cabecaHTTPS)




#for x in printavel:
 #   print(x)
#now first it has to be a connection to the host
#if successfull, we should see the host and the word or directory appended
"""
sendHTTPS = requests.get(ler)
for a in ler:
    print(host + a)
pedidoHTTPS = sendHTTPS.status_code
cabecaHTTPS = sendHTTPS.headers
pedido = send.status_code
cabeca = send.headers
def codigos():
    if pedido == 200 or pedidoHTTPS == 200:
        print("200 OK")
        print(cabeca)
        print(cabecaHTTPS)
    if pedido == 404 or pedidoHTTPS == 404:
        print("404 NOT FOUND")
    if pedido == 403 or pedidoHTTPS == 403:
        print("403 FORBIDDEN")
    if pedido == 301 or pedidoHTTPS == 301:
        print ("301 FOUND")
    if pedido == 401 or pedidoHTTPS == 401:
        print ("401 UNAUTHORIZED")
    else:
        print(pedido)
        print(pedidoHTTPS)
codigos()
"""