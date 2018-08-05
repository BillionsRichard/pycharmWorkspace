import json

"""
json 字符串必须是双引号。

1）json.dumps(obj,...)       ===> python对象转换成json字符串。
   json.dump(obj, fileObj)   ===> python对象转换成json字符串,并写入到文件对象fileObj中。

2) json.loads(json_str)      ===> json字符串转换成python对象。
   json.load(fileObj)       ====> 从文件中读取json字符串内容并转换成python对象。
"""
dict = {'name': 'Eva Cheung'}

data = json.dumps(dict)
print(data)
print(type(data))

class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


stu = Student('张长山', 32, '男')
stu_json = json.dumps(stu)

print(type(stu_json))
print(stu_json)
