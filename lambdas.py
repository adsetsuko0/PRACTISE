x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(4,3))

def myfunc(n):
    return lambda a:a*n
md=myfunc(2)
print(md(11))