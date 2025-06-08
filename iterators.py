mytupl=('apple','banana','grapes')
myit=iter(mytupl)
print(next(myit))
print(next(myit))

mystr='banana'
myit2=iter(mystr)
print(next(myit2))
print(next(myit2))

def my_generator():
    print('Start')
    yield 1
    print('After first yield')
    yield 2
    print('After second yield')

g=my_generator()
print(next(g))
print(next(g))



#генератор
def generator1(nums):
    index=0
    while index<nums:
        yield index
        index+=1

r=generator1(4)
print(next(r))
print(next(r))


