# 无需声明类型,直接赋值即可

str = '333333'
print(str)

# 连续赋值
a = b = c = 5
print('连续赋值',a,b,c)

# 多个变量赋值
a, b, c = 1, 2, 3
print('多个变量赋值', a,b,c)

# 魔术变量
print(__name__) # __main__
print(__file__)
# 删除变量引用
del a
# 类型检测
print(type(b) == int)
isinstance(b, int)