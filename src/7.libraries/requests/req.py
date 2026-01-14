import requests 

r = requests.get('https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests')

print(r.text)