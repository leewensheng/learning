import functools
from inspect import itertools

aaa = 3
bbb = 4
c = {aaa,bbb, aaa}
e , f = c
print(e, f)
print(type(c))

def fn():
  pass
class MyClass:
  @staticmethod
  def a():
    pass
print(type(fn))
print(type(MyClass.a))
