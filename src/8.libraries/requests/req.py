import requests 

url = "http://localhost:8000/home"
while True:
    r = requests.get(url)
    print(r.status_code)