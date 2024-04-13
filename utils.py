import re
import json


def extract_department_from_text(response):
    # 使用正则表达式提取尖括号（<>）之间的内容
    departments_text = re.search(r'<([^>]*)>', response).group(1)

    # 将提取的内容按管道符（|）分割为列表
    departments = [department.strip() for department in departments_text.split('|')]
    
    return departments

#extract the department from llm response
def extract_departments_from_json(data):
    departments = []
    json_data = json.loads(data)
    for key, value in json_data.items():
        if "department" in key:
            departments.append(value)
    return departments
    
#extract the activities from llm response
def extract_activities(data, activities):
    # row_data = eval(data)
    domain_json = json.loads(data)
    activities_list = domain_json["activities"]
    for i in range(len(activities_list)):
        if i < 2:
            activity = activities_list[i]
            activities.append(activity)
        else:
            break
    # print(activities)
    return None

#extract Order Process example from json
def extract_process_example(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    data = json.dumps(json_data) #dict type covert to str
    return data
    

