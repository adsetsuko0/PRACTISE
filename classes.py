class Cars:
    marka=""
    color='red'

bmw=Cars()
bmw.marka='BMW'
bmw.color='black'

print(f'He has a {bmw.color} {bmw.marka}')

class Room:
    length=0.0
    width=0.0

    def ploszczad(self):
        print('Area of the room is', self.length*self.width)

mojclass=Room()
mojclass.length=15
mojclass.width=18

mojclass.ploszczad()


class Person:
    name=''
    age=0
    sex=''

tom=Person()
tom.name='Tom'
tom.age=19
tom.sex='male'
print(f'Hello!I\'m {tom.name},i\'m {tom.age} years old')


class MyClass:
    attr1=10
    attr2='hello'

    def method1(self):
        print(MyClass.attr1)

    def method2(self):
        print(MyClass.attr2)


class MyBike:
    def __init__(self,name):
        self.name=name

bike1=MyBike('BMW')
print(bike1.name)

class Person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name},{self.age} years"

tom=Person1('n',18)
tom.age=10
print(tom.name)
print(tom.age)
print(tom)

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
print(hasattr(p1,'name'))
print(getattr(p1,'name'))
setattr(p1,'age',49)
print(p1.age)


class Person:
    def __init__(man,name):
        man.name=name
        print('Создание человека с именем',man.name)

    def __del__(man):
        print('Удален человек с именем ',man.name)


def create():
    p1=Person('Tom')

create()
print('The end.')

#С атрибутами экземпляров класса можно работать через такие функции:
#getattr(obj, name [, default]) — возвращает значение атрибута объекта;
#hasattr(obj, name) — проверяет на наличие атрибута name в obj;
#setattr(obj, name, value) — задает значение атрибута (если атрибут не существует, то он создается);
#delattr(obj, name) — удаляет атрибут с именем name.
#isinstance(obj, class) - позволяет определить принадлежность экземпляра к тому или иному классу

#Эти же операции можно делать и с самим классом.

class Point3D:
    x=100
    y=100
    z='301'
Point3D.z=000

delattr(Point3D,'z')

p1=Point3D()
p1.z=500
print(p1.x,p1.y,p1.z)

p2=Point3D()
p2.z=10
print(p2.x,p2.y,p2.z)

p3=Point3D()
p3.z=120
print(p3.x,p3.y,p3.z)

print(dir(p3))


class Car:
    car_count=0
    def start(self,name,model,year):
        print('The engine is running')
        self.name=name
        self.model=model
        self.year=year
        Car.car_count+=1

carA=Car()
carB=Car()
carA.start('Toyota','Corolla',2000)
carB.start('BMW','X3',2008)
print(carA.car_count,carA.name)
print(carB.car_count)


class A:
    def __init__(self):
        self.val='init'
class B(A):
    def __new__(cls, self):
        self.val='new'
        return self

c=B(A())
print(c.val)

class A:
    def __init__(self):
        self.val='init'
class B(A):
    def __new__(cls):
        return super().__new__(B)

c=B()
print(c.val)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
       return f'Name:{self.name}   Age:{self.age}'

class Employee(Person):
    def __init__(self,name,age,position):
        super().__init__(name,age)
        self.position=position

    def __str__(self):
        return f'{super().__str__()}  Position:{self.position}'

emp=Employee('Alice',40,'developer')
print(emp)

class DefaultDict(dict):
    def __missing__(self, key):
        return key

d=DefaultDict({1:1})
d[2]=d[3]
print(d)


num=10
new_num=num.__add__(5)
print(new_num)

class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000

    def __str__(self):
        return 'name='+self.name+', salary=$'+str(self.salary)

e1 = Employee()
print(e1)

class Distance:
    def __init__(self,x=None,y=None):
        self.ft=x
        self.inch=y
    def __add__(self, x):
        temp=Distance()
        temp.ft= self.ft + x.ft
        temp.inch= self.inch + x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft:' + str(self.ft) + ' in: ' + str(self.inch)
d1=Distance(3,10)
d2=Distance(4,4)
print("d1= {} d2={}".format(d1, d2))

d3=d1+d2
print(d3)