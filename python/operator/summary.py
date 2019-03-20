'''
python运算符分为
    算术运算符 加减乘除求余 整除  幂 以及他们的+= -= **= //= /= %=
    比较运算符 == != <>  < >  <= >=  
    位运算符 与& 或| 异或~  取反~ 左移<< 右移>>
    成员运算符 in not in (列表或字符串中)
    身份运算符 is    is not (指标比较)
python中没有自增运算符，如++a, a++ a-- --a
多了一个整除取整除 // 以及幂运算a**b
python中逻辑表达式使用and or  not
python的==比较的内容， 指针比较使用is is not
python中没有三目运算符?,使用 a = 1 if (b > 5 ) else 0
'''
a = [1,2]
print(a == [1,2]) # return True
print(a is [1,2]) # return False
print(1 in [1,2])