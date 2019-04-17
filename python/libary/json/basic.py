import json
import os

'''
json.dump()
json.loadd

json.dumps
json.loads
另有第三方库 demjson encode, decode方法
'''
path = os.getcwd()

dict1 = {'a': 3, 'b':'test'}
list1 = [1,2,3]
print(json.dumps(dict1))
print(json.dumps(list1))

jsonstr = '{"a":3}'
print(json.loads(jsonstr))

# 文件操作
path =  os.path.abspath(os.path.join(__file__,'../test.json'))
fd = open(path,'r')
dict1 = json.load(fd)

writePath = os.path.abspath(os.path.join(__file__, '../blank.json'))
fr = open(writePath, 'w')
json.dump({"dddd":'ddddd'},fr)

