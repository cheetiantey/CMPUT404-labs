import requests

req = requests.get("https://raw.githubusercontent.com/cheetiantey/CMPUT404-labs/main/request_version.py")

print(req.text)
