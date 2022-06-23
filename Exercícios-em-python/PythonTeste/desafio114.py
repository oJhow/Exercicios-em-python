import requests

def site():
    #verificar conexão do site Pudim
    url = 'http://www.pudim.com.br/'
    timeout = 5
    try:
        requests.get(url,timeout=timeout)
        return True
    except (ConnectionError):
        return False


if not site():
    print('O site está fora do ar')
else:
    print('O site pudim está funcionando normalmente.')

'''import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessível.')
else:
    print('O site Pudim está com sendo acessado normalmente.')
    print(site.read())'''
