#using sys
import sys
print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\nПеременная pythonpath содержит:',sys.path,'\n')

#example.py
def add(a,b):
    res=a+b
    return res

print(add(4,5))

#time
import time
time.sleep(3)
print('hello')

#datetime
import datetime as d
print(d.datetime.now().time())

#custome module
import mymodule as my
print(my.name)