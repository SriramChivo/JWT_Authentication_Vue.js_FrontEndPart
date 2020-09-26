import requests
import json
primary_url = "http://127.0.0.1:8000/"
secondary_url = "api/api-token-auth/"
sec = "api/1/"
data = json.dumps(
    {
        "username": "chivo",
        "password": "Chivo@07"
    }
)
headers = {
    "content-type": "application/json"
}
# print(type(data))
find = requests.post(primary_url+secondary_url, data=data, headers=headers)
print(find)
res = find.json()
# print(res)
print(res["token"])
token = res["token"]
headersToken = {
    "content-type": "application/json",
    "Authorization": "JWT "+token
}
find1 = requests.get(primary_url+sec, headers=headersToken)
print(find1)
res1 = find1.text
print(res1)
