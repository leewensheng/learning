# 普通函数定义
def fn(a, b):
  print(a,b)

fn(1,2)

# 默认参数
def fn2(a, b = 3):
  print(a, b)


# 可变参数,类似于js中的剩余参数,返回一个tulple
def fn3(a, *b):
  print(b)

fn3(1, 3, 4,5)
a=[100,200,300]
fn3(*a) # 类似于延展参数

# 关键字参数,返回一个dict,调用时给出参数名
def fn4(a, **b):
  print(b)

fn4(1, e=3, b=4, c=5)

# 命名关键字参数,使用*作为分隔
def fn5(a, *, d, b):
  print(d, b)

fn5(1, b = 3, d = 5)

# 各种参数顺序,必选参数,默认参数,可变参数, 命名关键字参数,关键字参数
