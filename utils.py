import re
import json


def extract_department_from_text(response):
    # 使用正则表达式匹配字段
    # fields = re.findall(r'([a-zA-Z]+\s[a-zA-Z]+)', response)
    
    # 将匹配到的字段放入列表中
    # departments = [field[0] if field[0] else field[1] for field in fields]

    # 使用正则表达式提取尖括号（<>）之间的内容
    departments_text = re.search(r'<([^>]*)>', response).group(1)

    # 将提取的内容按管道符（|）分割为列表
    departments = [department.strip() for department in departments_text.split('|')]
    
    return departments

#extract the department from llm response
def extract_departments_from_json(json_data):
    departments = []
    data = json.loads(json_data)
    for key, value in data.items():
        if "department" in key:
            departments.append(value)
    return departments
    
#extract the activities from llm response
def extract_activities_from_json(json_data):
    pass