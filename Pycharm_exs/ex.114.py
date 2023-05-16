import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://pudim.com.br')
except urllib.error.URLError:
    print('O site não está disponivel')
else:
    print('O site está funcionando')