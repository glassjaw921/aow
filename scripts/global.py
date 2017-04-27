x = 6
def nonGlobal():
    globx = x
    print(globx)
    globx+=5
    print(globx)
    return globx
x = nonGlobal()
print(x)
print('test')