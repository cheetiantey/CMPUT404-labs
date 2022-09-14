import requests

print(requests.__version__)

req = requests.get("http://www.google.com/")

print(req.text)
