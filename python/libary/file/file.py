import os
# http://www.runoob.com/python/python-files-io.html
# http://www.runoob.com/python/python-os-path.html
'''
python文件读写使用open操作符产生的file对象
基本的重命名, 删除,创建目录,切换目录, 使用os模块
'''
path = os.path.abspath(os.path.join(__file__,'../test.txt'))
fo = open(path,'w')
fo.write('这是一个测试文件')
fo.close()