import requests
import sys

# I need a host and then append the list from command line

#list can only contain some word or an "/" after the word
ler = open(sys.argv[1], 'r')
#printavel = ler.read()



for url in ler:
    site = "<site>"
    sendHTTPS = requests.get(site + str(url))
    pedidoHTTPS = sendHTTPS.status_code
    cabecaHTTPS = sendHTTPS.headers
    pedido = sendHTTPS.status_code
    cabeca = sendHTTPS.headers
    print (site + str(url) + "\n" + str(pedidoHTTPS))
    print (cabecaHTTPS)
