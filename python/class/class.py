# http://www.runoob.com/python3/python3-class.html

class Person:
  def __init__(self, name):
    self.name = name
  def getName(self):
    print(dir(self))
    print('class Name is %s' % self.__class__.__name__)
    return self.name

b = Person('liwensheng')
print(b.getName())