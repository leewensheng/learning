# 列表, 可以使用加法与乘法运算符达到连接与重复的效果
# http://www.runoob.com/python/python-lists.html
a = [1,2,3,2]
b = (1,2,3,4,5)
print(a + list(b))
print(a * 3)
print(len(a))
print(a.count(2))
print(max(a))
print(min(a))
print(list(b))

def square(x):
  return x*x
arrmap = map(square, a)
print(list(arrmap))
print(type(33))