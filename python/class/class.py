# http://www.runoob.com/python3/python3-class.html

class Person:
  def __init__(self, name):
    self.name = name
  def getName(self):
    return self.name

b = Person('liwensheng')
print(b.getName())