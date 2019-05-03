class MyClass:
    def __fn(self): # 私有方法不允许在外部调用
        print('test')
    



a = MyClass()
a.__fn() # 会报不存在的方法
