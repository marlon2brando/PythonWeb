import json

student = {'name':'marlon','age':25}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))

print('JSON对象:{0}'.format(stu_json))

stu_dic = json.loads(stu_json)
print(type(stu_dic))
print(stu_dic)


# 读取json的文件



data = {'name':"hahah",'age':12}

with open('t.json','w') as f:
    json.dump(data,f)

with open('t.json','r') as f:
    print(f.read())