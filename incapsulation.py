class MyClass:
    def __init__(self):
        self._protectedattr='I am protected'
        self.__privateattr='I am private'

    def get_privateattr(self):
        return self.__privateattr

    def set_privateattr(self,value):
        if isinstance(value,str):
            self.__privateattr=value

obj=MyClass()
print(obj.get_privateattr())
obj.set_privateattr('Some value here')
print(obj.get_privateattr())

class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    # сеттер для установки возраста
    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    # геттер для получения возраста
    def get_age(self):
        return self.__age

    # геттер для получения имени
    def get_name(self):
        return self.__name

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.print_person()  # Имя: Tom  Возраст: 25

#геттеры и сеттеры
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if 0<age<110:
            self.__age=age
        else:
            print('Invalid age')

    @property
    def name(self):
        return self.__name

    def print_name(self):
        print(f'Name:{self.__name}\t Age:{self.__age}')

p1=Person('Anna',18)
p1.print_name()
p1.age=-19
print(p1.age)

class Book:
    def __init__(self,title,author):
        self.__title=title
        self.__author=author

    def get_title(self):
        return self.__title

    def set_title(self,title):
        self.__title=title

    def get_author(self):
        return self.__author

    def set_author(self,author):
        self.__author=author


book1=Book('Voina i mir','Lev Tolstoi')
print(book1.get_title())
book1.set_title('Idk')
print(book1.get_title())

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'


st=Student('Anna','20')
print(st.name)
print(st.gotmarks)
st.name='Alena'
print(st.name)
print(st.gotmarks)

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount

    @property
    def balance(self):
        return self.__balance

acc=BankAccount(100)
acc.deposit(50)
print(acc.balance)
acc.withdraw(30)
print(acc.balance)

class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def check(self,password):
        return self.__password==password

user=User('john','1234')
print(user.username)
print(user.check('1234'))

class Rectangle:
    def __init__(self,length,width):
        self.__length=length    #заприватила
        self.__width=width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self,value):
        self.__length=value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width=value

    def perimetr(self):
        return 2*(self.__length + self.__width)

    def ploszczad(self):
        return self.__length* self.__width

p1=Rectangle(10,20)
p2=Rectangle(5,10)
print(f'Длины двух прямоугольников:{p1.length},{p2.length}')
print(f'Периметр первого прямоугольника:{p1.perimetr()}')
print(f'Периметр второго прямоугольника:{p2.perimetr()}')
print(f'Площадь первого прямоугольника:{p1.ploszczad()}')
print(f'Площадь второго прямоугольника:{p1.ploszczad()}')


class Student:
    def __init__(self,name):
        self.name=name
        self.__grades=[]

    def add_grade(self,grade):
        if 0<grade<100:
            self.__grades.append(grade)

    def av(self):
        return sum(self.__grades)/ len(self.__grades) if self.__grades else 0

st1=Student('Alice')
st1.add_grade(90)
st1.add_grade(85)
print(st1.av())