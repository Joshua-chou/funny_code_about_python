'''
L : location 函数内部作用域
E : enclosing 函数内部与内嵌函数之间
G : global  全局作用域
B : build-in 内置作用域
'''

passline = 60   # 全局
def func(val):
    passline = 90   # 局部
    if val > passline:
        print('pass')
    else:
        print('fail')
func(61)

def m(a,b):       # 内置
    return max(a,b)
print(m(1,2))

def function(a):   # 函数内部与内嵌函数之间
    def inner():
        print('this is %s'%(a))
    return inner
a = function(5)
a()
