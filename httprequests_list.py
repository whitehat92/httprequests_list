import requests
import sys

headers = {'User-Agent': 'Mozilla/12.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
list = open(sys.argv[1], 'r')
for url in list:
    target = open(sys.argv[0], 'r')
    site = "<website"
    sendHTTPS = requests.get(site + str(url), timeout=10, headers=headers)
    pedidoHTTPS = sendHTTPS.status_code
    cabecaHTTPS = sendHTTPS.headers
    print (str(pedidoHTTPS) + "<------>" + site + str(url) + str(cabecaHTTPS))
