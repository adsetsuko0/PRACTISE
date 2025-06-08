#декораторы
def check(func):
    def wrapper(*args):
        name=args[0]
        age=args[1]
        if age<0:age=1
        func(name,age)
    return wrapper

def check1(func):
    def wrapper(*args):
        res=func(*args)
        if res<0: res=0
        return res
    return wrapper

def uppercasedec(func):
    def wrapper():
        orig=func()
        modified=orig.upper()
        print(modified)
    return wrapper

def select(input_func):
    def output_func():      # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()                # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки
    return output_func

def strong(func):
    def wrapper():
        return '<strong>'+ func() +'</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>'+ func() +'</em>'
    return wrapper

def trace(func):
    def wrapper(*args,**kwargs):
        print(f'TRACE: calling {func.__name__}()'
              f' with {args} ,{kwargs}')

        orig=func(*args,**kwargs)

        print(f'TRACE: {func.__name__}()'
              f' returned {orig}')

        return orig
    return wrapper

#конец декораторов
@select
def greet():
    print('Hello!')

greet()


@trace
def say(name,line):
    return f'{name}:{line}'

print(say('Anna','hello'))

@check
def hello(name,age):
    print(f'Name:{name} age:{age}')

hello('anna',18)

def sum(a,b):
    return a+b

