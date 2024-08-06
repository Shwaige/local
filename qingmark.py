import requests
from jsonpath_ng import parse

url = 'https://qingflow.com/api/connector/all'
token = 'token'  # token
wsId = 'wsId'  # wsId
headers = {'Content-Type': "application/json", "token": token, "wsId":wsId}
response = requests.get(url=url, headers=headers)
data = response.json()
jsonpath_expr = parse('$.data.openAppList[*].id')
matches = jsonpath_expr.find(data)

# print(ids)
k = []
h = []
for i in matches:
    url = 'https://qingflow.com/api/connector/{}'.format(i.value)
    response = requests.get(url=url, headers=headers)
    data = response.json()
    jsonpath_expr2 = parse('$.data.auth.authType')
    jsonpath_expr3 = parse('$.data.name')

    auth_types = jsonpath_expr2.find(data)
    if auth_types and auth_types[0].value == 4:
        descriptions = jsonpath_expr3.find(data)
        if descriptions:
            h.append(descriptions[0].value)

print(k)
print(h)
