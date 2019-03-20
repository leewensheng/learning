'''
python自动识别变量是局部还是全局的，
在函数如果局部变量和全局变量冲突
，为消除歧义，使用global声明,
python的全局变量只存在于当前文件中，无法跨文件（可用模块实现）
'''
g_var = 1
def fn():
    g_var = 2
    print('fn1，未改变全局变量',g_var) 

def fn2():
    global g_var
    g_var = 3
    print('fn2，global声明，改变全局变量',g_var)

fn()
print(g_var)
fn2()
print(g_var)