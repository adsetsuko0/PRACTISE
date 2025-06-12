from math import pi
from abc import ABC, abstractmethod

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


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return 'Meow'

class Dog(Animal):
    def speak(self):
        return 'Woof'

class Bird(Animal):
    def speak(self):
        return 'Tweet'

class Fish(Animal):
    def speak(self):
        return 'No sound'

def animals_speaking(animals):
    for an in animals:
        print(an.speak())

def make_animal_speak(animal):
    print(animal.speak())

dog=Dog()
cat=Cat()
fish=Fish()
bird=Bird()
animals_speaking([dog,cat,bird,fish])

class Calculator:
    def add(self, a,b=0):
        return a+b

calc=Calculator()
print(calc.add(1,6))


from multipledispatch import dispatch
class ShapeCalculator:
    @dispatch(float)
    def calculate_area(self,radius):
        return 3.14*radius*radius

    @dispatch(float,float)
    def calculate_area(self,length,width):
        return length*width

    @dispatch(float,float,float)
    def calculate_area(self,a,b,c):
        s=(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

calc=ShapeCalculator()
print(calc.calculate_area(5.0))
print(calc.calculate_area(9.0,0.0))
print(calc.calculate_area(4.0,7.0,8.0))

class PaymentProcessor:
    def process_payment(self,amount):
        raise NotImplementedError("Подкласс должен реализовать абстрактный метод")

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self,amount):
        print(f"Обработка оплаты банковской картой на сумму ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self,amount):
        print(f"Обработка оплаты PayPal на сумму ${amount}")

class BitcoinProcessor(PaymentProcessor):
    def process_payment(self,amount):
        print(f"Обработка оплаты Bitcoin на сумму ${amount}")

def checkout(cart,payment_processor):
    total=sum(item.price for item in cart)
    payment_processor.process_payment(total)



class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('недостаточно средств')

    def get_balance(self):
        return self.__balance

my_account=BankAccount()
my_account.deposit(1000)
my_account.withdraw(500)
print(my_account.get_balance())

def calculate_area(shape, *args):
    if shape=='circle':
        return 3.14 * args[0] **2
    elif shape=='rectangle':
        return args[0] * args[1]
    elif shape=='triangle':
        return 0.5 * args[0] * args[1]
    else:
        return 'invalid form'

circle_area=calculate_area('circle', 8)
rectangle_area=calculate_area('rectangle', 89, 90)
print(f"Площадь круга: {circle_area}")
print(f"Площадь прямоугольника: {rectangle_area}")

class Book(ABC):
    def __init__(self,title,author,year):
        self.title=title
        self.year=year
        self.author=author

    @abstractmethod
    def get_summary(self):
        pass

class Fiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - роман в стиле исторический фикшн, автор - {self.author}')

fiction_book = Fiction("Террор", "Дэн Симмонс",2007)
fiction_book.get_summary()