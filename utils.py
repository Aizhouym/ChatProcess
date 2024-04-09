import re



def get_specific_domains(response):
    # 使用正则表达式匹配字段
    # fields = re.findall(r'([a-zA-Z]+\s[a-zA-Z]+)', response)
    
    # 将匹配到的字段放入列表中
    # departments = [field[0] if field[0] else field[1] for field in fields]

    # 使用正则表达式提取尖括号（<>）之间的内容
    departments_text = re.search(r'<([^>]*)>', response).group(1)

    # 将提取的内容按管道符（|）分割为列表
    departments = [department.strip() for department in departments_text.split('|')]
    
    return departments

# test for the extraction from DoaminAnswer
# print(get_specific_domains("DomainAnswer:Emergency Departments < Fire Department | Forestry Department | Emergency Medical Services >"))
