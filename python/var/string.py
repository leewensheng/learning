import re


a = '333'
a = "3333"
a = '\'33'
a = '\"33333'
a = r'\n\t' # 不转义字符串
a = u'this is a unicode' # unicode字符串

a = '''
3333333
dddd
'''

a = """dddd
ddfdsfd
"""

print(a[2])
print(a[2:4])
print(a + '3333')

b = a * 2 #字符串repeat
c = '3' in b #判断包含
c = '5' not in b
d = r'\nfdsfdfd' # 不转义字符串,R亦可
format = '55322%s' % ('python')
print(format)
print(len('3333'))
