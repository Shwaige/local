import requests

url = 'https://develop-test.oalite.com/ultronapi/skill/list?appId=264267359766675458'
headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'qf-request-id': '21abec52-ade5-4597-bd12-deb1ea0b4ea5',
    'token': '18d479f6-5c86-4c7e-8473-e01666f3930d',
    'wsid': '3771'
}

response = requests.get(url, headers=headers)

data = response.json()

# 提取 'data' 数组
skill_array = data.get('data', [])  # 获取 data 数组

# 提取每个技能的 'id' 值
ids = [skill.get('associationId') for skill in skill_array]

print(ids)

for i in ids:
    url = "https://develop-test.oalite.com/ultronapi/skill/delete"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'qf-request-id': '21abec52-ade5-4597-bd12-deb1ea0b4ea5',
        'token': '18d479f6-5c86-4c7e-8473-e01666f3930d',
        'wsid': '3771'
    }

    # 将 body 定义为字典
    body = {"associationId": i}

    # 使用 json 参数而不是 data 参数将 body 转换为 JSON
    response = requests.post(url=url, headers=headers, json=body)
    print(response.json())
