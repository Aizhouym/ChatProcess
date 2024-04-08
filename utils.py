import re



def get_specific_domains(response):
    # 使用正则表达式匹配字段
    fields = re.findall(r'Field\d+: (.*?) \||Field\d+: (.*?) >', response)

    # 将匹配到的字段放入列表中
    departments = [field[0] if field[0] else field[1] for field in fields]
    
    return departments
