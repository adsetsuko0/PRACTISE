from datetime import MAXYEAR


class Addition:
    first=0
    second=0
    summa=0

    def __init__(self,f,s):
        self.first=f
        self.second=s

    def vyvod(self):
        print('First num:',self.first)
        print('Second num:', self.second)
        print('Addition of two these:', self.summa)

    def calculate(self):
        self.summa=self.first + self.second


nums=Addition(40,30)
nums.calculate()
nums.vyvod()

class MyClass:
    def __init__(self,name=None):
        if name is None:
            print('The default constructor called')
        else:
            self.name=name
            print('The parametrised constructor called')

    def method(self):
        if hasattr(self,'name'):
            print('The method is called with name', self.name)
        else:
            print('The method\'s called without a name')

obj1=MyClass()
obj2=MyClass('Anna')
obj2.method()

class Vector:
    MIN=0
    MAX=100

    def __init__(self,x,y):
        self.x=self.y=0
        if Vector.validate(x) and Vector.validate(y):
            self.x=x
            self.y=y


    @classmethod
    def validate(cls,arg):
        return cls.MIN<= arg<= cls.MAX

res=Vector.validate(5)
print(res)


class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    @classmethod
    def create_from_list(cls, arg_list):
        return cls(arg_list[0], arg_list[1])


mylist=[1,6,79,42,678]
obj=MyClass.create_from_list(mylist)
print(obj.arg2)

class MyClass:
    class_attr='class_attr_value'

    @classmethod
    def method1(cls):
        print(cls.class_attr)

MyClass.method1()

class Point3D:
    coordinates=[]
    def __init__(self,x=0,y=0,z=0): #атрибуты класса
        self.x=x
        self.y=y
        self.z=z

    def get_list(self):
        if type(self.x)==int and type(self.y)==int and type(self.z)==int: #проверка типов данных
            Point3D.coordinates.append(self.x)
            Point3D.coordinates.append(self.y)
            Point3D.coordinates.append(self.z)
        else:
            print('Wrong type!')

    def get_cords(self):
        res_str=(self.x,self.y,self.z)  #координаты в виде кортежа
        return res_str

    def change_cords(self):
        try:
            x_str, y_str, z_str = input("Введите новые координаты для " + str(self.__doc__) + "\n").split()
            self.x = int(x_str)
            self.y = int(y_str)
            self.z = int(z_str)
        except ValueError:
            print("Ошибка:требуется ввести ТРИ целых числа через пробел.")

class Point(Point3D):
    pass

pt1 = Point3D(5, 2, 5)
pt2 = Point3D(2, 6, 3)
pt3 = Point3D(2, 5, "s")
pt4 = Point(*pt1.get_cords())
pt5 = Point()


class Dog:
    def __init__(self,name):
        self.name=name
        self.tricks=[]

    def tricksadd(self,trick):
        self.tricks.append(trick)


b=Dog('Bobby')
b.tricksadd('Roll over')
print(b.tricks)

class Father:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def printname(self):
        print(self.name,self.lastname)

class Son(Father):
    pass

tom=Son('Tom','Huesos')
tom.printname()


class Father:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def printname(self):
        print(self.name,self.lastname)

class Son(Father):
    def __init__(self,name,lastname):
        super().__init__(name,lastname)


x=Son('Make','User')
x.printname()


class Geom:
    name='geom'

    def __init__(self):
        print('Geom initializator')
class Line(Geom):
    def draw(self):
        print('Drawing a line')
i=Line()


class Human:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def printname(self):
        print('Tha\'s a superclass')

class Person(Human):
    def printname(self):
        super().printname()
        print('That\'s a subclass')

x=Person('Anna',"Ermak")
x.printname()

class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name):
        Person.__init__(self,name)


y=Student('Anna')

class Computer:
    def __init__(self,computer,ram,ssd):
        self.computer=computer
        self.ram=ram
        self.ssd=ssd


class Laptop(Computer):
    def __init__(self,computer,ram,ssd,model):
        super().__init__(computer,ram,ssd)
        self.model=model

lenovo=Laptop('Lenovo',2,512,1420)
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)


class Rectangle:
    def __init__(self,width,length):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*self.length+2*self.width

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

sqr=Square(4)
print('Area of the square is ',sqr.area())


class A:
    def __init__(self):
        print('Initializing class A')

    def sub_method(self,b):
        print('Sub_method from class A:',b)

class B(A):
    def __init__(self):
        print('Initializing class B')
        super().__init__()

    def sub_method(self,b):
        print('Sub_method from class B:',b)
        super().sub_method(b+1)

class X(B):
    def __init__(self):
        print('Initializing class X')
        super().__init__()

    def sub_method(self,b):
        print('Sub_method from class X:',b)
        super().sub_method(b+1)

class Y(X):
    def __init__(self):
        print('Initializing class Y')
        super(X, self).__init__()

    def sub_method(self,b):
        print('Sub_method from class Y:',b)
        super().sub_method(b+1)

x = X()
x.sub_method(1)
y=Y()
y.sub_method(5)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'Person:{self.name}, age:{self.age}'

    def __eq__(self, other):
        if isinstance(other,Person):
            return self.age==other.age
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Person):
            return self.age != other.age
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented








person1=Person('Alice',20)
person2=Person('Tom',18)
person3=Person('Bob',27)
print(f"{person1} == {person2}: {person1 == person2}")
print(f"{person1} != {person2}: {person1 != person2}")
print(f"{person2} < {person1}: {person2 < person1}")
print(f"{person2} <= {person3}: {person2 <= person3}")
print(f"{person1} > {person2}: {person1 > person2}")
print(f"{person1} >= {person3}: {person1 >= person3}")

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return f'Vector {self.x},{self.y},{self.z}'

    def __add__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Умножение на скаляр
            return Vector(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Деление на ноль недопустимо.")
            return Vector(self.x / other, self.y / other, self.z / other)
        return NotImplemented

        # Чтобы работало умножение скаляр * вектор

    def __rmul__(self, other):
        return self.__mul__(other)

    # Пример использования
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(3 * v2)
print(v2 / 2)



class Vehicle:
    def __init__(self, marka, model, year, value):
        self.marka=marka
        self.model=model
        self.year=year
        self.value=value

    def display_info(self):
        print(f'The vehicle {self.marka},the model {self.model} of {self.year} was {self.value}')


class Car(Vehicle):
    def __init__(self,marka,model,year,value,doors):
        super().__init__(marka,model,year,value)
        self.doors=doors

    def display_info(self):
        print(f'The car {self.marka},the model {self.model} of {self.year} was {self.value}')

class Truck(Vehicle):
    def __init__(self,marka,model,year,value,length):
        super().__init__(marka,model,year,value)
        self.length=length

    def display_info(self):
        print(f'The truck {self.marka},the model {self.model} of {self.year} was {self.value} has the length about'
              f' {self.length}')

car = Car("Toyota", "Camry", 2022, 2900000, 4, )
truck = Truck("Ford", "F-MAX", 2023, 6000000, 6162)
car.display_info()
truck.display_info()
