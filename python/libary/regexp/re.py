# http://www.runoob.com/python/python-reg-expressions.html
import re
# 匹配成功时返回一个matchObject,失败时返回None
# match 从起始位置匹配
# search 扫描整个字符串并返回第一个成功的匹配
a = 'www.baidu.com'
re.match(pattern, string, flags=0)
re.search()
re.sub()
re.subn()
re.escpae()
re.split()
re.finditer()
re.findall
re.purge()
re.compile(pattern, flags=0)
re.M
re.I
re.L
re.U
re.X
re.S