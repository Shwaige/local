import json

# 原始数据
data = {
    "tableValues": [
        [
            {
                "queId": 305458832,
                "queType": 2,
                "queTitle": "单行文字",
                "values": [{"value": "text1"}],
                "referValues": [],
                "tableValues": []
            },
            {
                "queId": 305458833,
                "queType": 8,
                "queTitle": "数字",
                "values": [{"value": "1"}],
                "referValues": [],
                "tableValues": []
            },
            {
                "queId": 305458834,
                "queType": 3,
                "queTitle": "多行文字",
                "values": [{"value": "这是郭德纲1"}],
                "referValues": [],
                "tableValues": []
            }
        ],
        [
            {
                "queId": 305458832,
                "queType": 2,
                "queTitle": "单行文字",
                "values": [{"value": "text2"}],
                "referValues": [],
                "tableValues": []
            },
            {
                "queId": 305458833,
                "queType": 8,
                "queTitle": "数字",
                "values": [{"value": "2"}],
                "referValues": [],
                "tableValues": []
            },
            {
                "queId": 305458834,
                "queType": 3,
                "queTitle": "多行文字",
                "values": [{"value": "这是郭德纲2"}],
                "referValues": [],
                "tableValues": []
            }
        ]
    ]
}

# 生成 200 个元素
result = {"tableValues": []}
for i in range(1, 201):
    new_entry = [
        {
            "queId": 305458832,
            "queType": 2,
            "queTitle": "单行文字",
            "values": [{"value": f"text{i}"}],
            "referValues": [],
            "tableValues": []
        },
        {
            "queId": 305458833,
            "queType": 8,
            "queTitle": "数字",
            "values": [{"value": str(i)}],
            "referValues": [],
            "tableValues": []
        },
        {
            "queId": 305458834,
            "queType": 3,
            "queTitle": "多行文字",
            "values": [{"value": f"这是郭德纲{i}"}],
            "referValues": [],
            "tableValues": []
        }
    ]
    result["tableValues"].append(new_entry)

# 输出结果
print(json.dumps(result, ensure_ascii=False, indent=4))
