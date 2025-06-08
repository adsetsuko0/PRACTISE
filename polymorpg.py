from math import pi

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f'Hello! I\'m cat {self.name} and i\'m {self.age} years old')

    def sound(self):
        print('Meow')

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f'Hello! I\'m dog {self.name} and i\'m {self.age} years old')

    def sound(self):
        print('Woof')

cat1=Cat('Kitty',10)
dog1=Dog('Doggy',7)

for animal in (cat1,dog1):
    animal.sound()
    animal.info()
    animal.sound()


class Shape:
    def __init__(self,name):
        self.name=name

    def area(self):
        pass

    def fact(self):
        return 'i\'m a two-dimensional shape'

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self,length):
        super().__init__('Square')
        self.length=length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

class Circle(Shape):
    def __init__(self,radius):
        super().__init__('Circle')
        self.radius=radius

    def area(self):
        return self.radius**2*pi

a=Square(4)
b=Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())