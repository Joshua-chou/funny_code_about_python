
def func_100(val):
    passline = 60
    if val >= passline:
        print('pass')
    else:
        print('fail')

def func_150(val):
    passline = 90
    if val >= passline:
        print('pass')
    else:
        print('fail')

# 合并
def fun(passline):
    def inner(val):
        if val >= passline:
            print('pass')
        else:
            print('fail')
    return inner

inn = fun(60)
inn(61)
