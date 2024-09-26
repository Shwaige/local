import concurrent.futures

import requests

url = "https://develop-test.oalite.com/ultronapi/skill/add"

headers = {'accept': 'application/json, text/plain, */*', 'content-type': 'application/json',
           'qf-request-id': '21abec52-ade5-4597-bd12-deb1ea0b4ea5', 'token': '18d479f6-5c86-4c7e-8473-e01666f3930d',
           'wsid': '3771'
           }
body = {"title": "123123", "icon": "https://file.qingflow.com/assets/ultron/icon/skill-icon1.png",
        "description": "啥的打扫打扫打的", "skillType": "CONTENT_PRODUCTION", "appId": "264267359766675458"
        }


# 定义一个函数来发送请求
def send_request():
    response = requests.post(url, headers=headers, json=body)
    return response.status_code, response.json()


# 使用 ThreadPoolExecutor 进行多线程并发请求
def send_multiple_requests(num_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # 提交多个请求任务
        futures = [executor.submit(send_request) for _ in range(num_requests)]

        # 等待任务完成并获取结果
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, response_json = future.result()
                print(f"Status Code: {status_code}, Response: {response_json}")
            except Exception as e:
                print(f"Request generated an exception: {e}")


# 发送并发请求
send_multiple_requests(30)
