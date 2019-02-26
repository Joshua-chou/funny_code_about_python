#
# def w1(func):
#     print('---w1---')
#     def inner():
#         print('---inner1')
#         func()
#     return inner
#
# def w2(func):
#     print('---w2---')
#     def inner():
#         print('---inner2')
#         func()
#     return inner
#
# @w1
# @w2
# def p():
#     print('---test1---')
#
# p()


# # 使用装饰器对有参数的函数进行装饰
# def w1(func):
#     def inner(*args, **kwargs):
#         print('---inner---')
#         func(*args, **kwargs)
#     return inner
#
# @w1
# def p(*args):
#     print(sum(args))
#
# p(1,2,3)

# # 装饰带有return的函数
# def w1(func):
#     def inner(*args):
#         print('---inner---')
#         return func(*args)
#     return inner
#
# @w1
# def p(a,b):
#     return a+b
#
# print(p(1,2))


class Test:                                     # 类装饰器
    def __init__(self,func):
        print("__init__")
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__func()

@Test
def test():
    print("--test--")

test()