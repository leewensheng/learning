import sys
import os
import module1.a as moda
import module2.b as modb
import pacage
# python分绝对导入和相对导入
# 绝对导入在当前目录和第三方包目录查找
# 相对导入根据当前__name__ 相对查找
# 作为执行中的包,__name__永远是__main__ 故不可以使用相对路径
# 作为被导的包,可以使用相对路径
# 包大全https://docs.python.org/zh-cn/3.6/py-modindex.html
time = __import__('time')
moda.a()
modb.b()
pacage.re
