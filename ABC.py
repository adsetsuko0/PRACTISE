import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length, height):
        self.length=length
        self.height=height

    def area(self):
        return self.length * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2*3.14

def print_area(shape):
    print('Area:', shape.area())

a=Rectangle(30,50)
c=Circle(30)
print_area(a)
print_area(c)

class Shape(abc.ABC):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @abc.abstractmethod
    def area(self):
        pass

    def print_area(self):
        print('X:',self.x,'\tY:',self.y)

class Rectangle(Shape):
    def __init__(self,x,y,length,height):
        super().__init__(x,y)
        self.length=length
        self.height=height

    def area(self):
        return self.length * self.height

rect=Rectangle(10,20,100,200)
rect.print_area()

class Recipe(abc.ABC):
    @abc.abstractmethod
    def cook(self):
        pass

class Entree(Recipe):
    def __init__(self,ingredients):
        self.ingredients=ingredients

    def cook(self):
        print(f"Готовим на медленном огне смесь ингредиентов ({', '.join(self.ingredients)}) "
        f"для основного блюда")

class Dessert(Recipe):
    def __init__(self,ingredients):
        self.ingredients=ingredients

    def cook(self):
        print(f"Смешиваем {', '.join(self.ingredients)} для десерта")

class Appetizer(Recipe):
    pass

class PartyMix(Appetizer):
    def cook(self):
        print("Готовим снеки - выкладываем на поднос орешки, чипсы и крекеры")

entree=Entree(['chicken','rise','veggies'])
dessert=Dessert(['ice-cream','chocolate chips'])
partymix=PartyMix()
entree.cook()
dessert.cook()
partymix.cook()

class Confectionary:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def decribe_dessert(self):
        print(f'{self.name} by the price {self.price}'
              f'rub/kg')

class Cake(Confectionary):
    def describe(self):
        print(f'The cake {self.name} was '
              f'{self.price} per kg')

class Candy(Confectionary):
    def describe(self):
        print(f'The candies {self.name} were'
              f'{self.price} per kg')

class Cookie(Confectionary):
    pass

cake=Cake('Prażskij',1200)
candy=Candy('Choco',560)
cookie=Cookie('Ovsyanoe',250)

cake.describe()
candy.describe()


class Beverage:
    def __init__(self,name,size,price):
        self._name=name
        self._size=size
        self._price=price

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def get_price(self):
        return self._price

    def describe(self):
        return (f'{self._size} '
         f'л газировки "{self._name}" стоит {self._price} руб.')

class Soda(Beverage):
    def __init__(self,name,size,price,flavour):
        super().__init__(name,size,price)
        self._flavour=flavour

    def get_flavour(self):
        return self._flavour

    def describe(self):
        return f'{self._size} л газировки "{self._name}" со вкусом "{self._flavour}" стоит {self._price} руб.'

class DietSoda(Soda):
    def __init__(self,name,size,price,flavour):
        super().__init__(name,size,price,flavour)

    def describe(self):
        return f'{self._size} л диетической газировки "{self._name}" со вкусом "{self._flavor}" стоит {self._price} руб.'

regular_soda=Soda('Sprite',0.33,45,'lemon')
print(regular_soda.describe())

class Starship(abc.ABC):
    @abc.abstractmethod
    def warp_speed(self):
        pass

    @abc.abstractmethod
    def fire_weapon(self):
        pass

    @abc.abstractmethod
    def self_destruct(self):
        pass

class FederationStarship(Starship):
    def warp_speed(self):
        print('Включить варп-двигатели!')

    def fire_weapon(self):
        print('Выпустить фотонные торпеды!')

    def self_destruct(self):
        print('Запускаю систему самоуничтожения...')

class KlingonWarship(Starship):
    def warp_speed(self):
        print('Включить маскировочное устройство!')

    def fire_weapon(self):
        print('Стрелять из фазеров!')

    def self_destruct(self):
        print('Запускаю протокол самоуничтожения...')

enterprice=FederationStarship()
bird_of_prey=KlingonWarship()

enterprice.warp_speed()
bird_of_prey.warp_speed()

enterprice.fire_weapon()
bird_of_prey.fire_weapon()

enterprice.self_destruct()
bird_of_prey.self_destruct()

class Ingredient(abc.ABC):
    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_quantity(self):
        pass

class Vegetable(Ingredient):
    def __init__(self,name,kolvo):
        self.name=name
        self.kolvo=kolvo

    def get_name(self):
        return self.name


    def get_quantity(self):
        return f'{self.kolvo} kg'

class Fruit(Ingredient):
    def __init__(self,name,kolvo):
        self.name=name
        self.kolvo=kolvo

    def get_name(self):
        return self.name

    def get_quantity(self):
        return f'{self.kolvo} kg'

veg=Vegetable('carrot',5)
fruit=Fruit('apple',10)

print(veg.get_name())
print(fruit.get_name())

print(veg.get_quantity())
print(fruit.get_quantity())


def validate_soldier(func):
    def wrapper(self):
        if not isinstance(self,Soldier):
            raise TypeError('Объект не в классе Soldier')
        return func(self)
    return wrapper

class Soldier(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def defend(self):
        pass



class Infantry(Soldier):
    @validate_soldier
    def move(self):
        print('Пехота передвигается в пешем порядке')

    @validate_soldier
    def attack(self):
        print('Пехота участвует в ближнем бою')

    @validate_soldier
    def defend(self):
        print("Пехота держит строй")



class Cavalry(Soldier):
    @validate_soldier
    def move(self):
        print("Кавалерия передвигается верхом")

    @validate_soldier
    def attack(self):
        print("Кавалерия переходит в атаку")

    @validate_soldier
    def defend(self):
        print("Кавалерия защищает фланги")

class Army:
    def __init__(self):
        self.soldiers=[]

    def add_soldier(self,soldier):
        self.soldiers.append(soldier)

    def attack(self):
        for soldier in self.soldiers:
            soldier.move()
            soldier.attack()

    def defend(self):
        for soldier in self.soldiers:
            soldier.move()
            soldier.defend()




def validate_dinosaur(func):
    def wrapper(self):
        if not isinstance(self,Dinosaur):
            raise TypeError('Объект не в классе Dinosaur')
        return func(self)
    return wrapper

class Dinosaur(abc.ABC):
    @abc.abstractmethod
    def get_personal_name(self):
        pass

    @abc.abstractmethod
    def get_breed(self):
        pass

    @abc.abstractmethod
    def get_height(self):
        pass

    @abc.abstractmethod
    def get_weight(self):
        pass

    @abc.abstractmethod
    def get_diet(self):
        pass


class Carnivore(Dinosaur):
    def __init__(self, name, breed, height, weight, ):
        self.name = name
        self.breed = breed
        self.height = height
        self.weight = weight

    def get_personal_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return 'Плотоядный'

class Herbivore(Dinosaur):
    def __init__(self, name, breed, height, weight):
        self.name = name
        self.breed = breed
        self.height = height
        self.weight = weight

    def get_personal_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return 'Травоядный'

class DinosaurPark:
    def __init__(self):
        self.dinosaurs=[]

    def add_dinosaur(self,dinosaur):
        self.dinosaurs.append(dinosaur)

    def list_dinosaurs(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_height(), dinosaur.get_weight(),
                 dinosaur.get_diet()) for dinosaur in self.dinosaurs]

    def list_carnivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_height(), dinosaur.get_weight(),
        dinosaur.get_diet()) for dinosaur in self.dinosaurs if isinstance(dinosaur, Carnivore)]

    def list_herbivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_height(), dinosaur.get_weight(),dinosaur.get_diet())
        for dinosaur in self.dinosaurs if isinstance(dinosaur, Herbivore)]

t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)
park = DinosaurPark()

park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)

for dinosaur in park.list_herbivores():
    print(f'Имя: {dinosaur[0]}\n'
    f'Вид: {dinosaur[1]}\n'
    f'Вес: {dinosaur[2]} кг\n'
    f'Рост: {dinosaur[3]} см\n'
    f'Рацион: {dinosaur[4]}\n')

class Instruments(abc.ABC):
    @abc.abstractmethod
    def get_name(self):
        pass
    @abc.abstractmethod
    def get_type(self):
        pass
    @abc.abstractmethod
    def get_sound(self):
        pass

class StringedInstrument(Instruments):
    def __init__(self,name,type,sound):
        self.name=name
        self.type=type
        self.sound=sound

    def get_sound(self):
        return self.sound
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type


class PercussionInstrument(Instruments):
    def __init__(self,name,type,sound):
        self.name=name
        self.type=type
        self.sound=sound

    def get_type(self):
        return self.type
    def get_sound(self):
        return self.sound
    def get_name(self):
        return self.name

class Orchestra:
    def __init__(self):
        self.instruments=[]

    def add_instruments(self,instrument):
        self.instruments.append(instrument)

    def list_instruments(self):
        return [instrument.get_name() for instrument in self.instruments]

    def list_stringed_instruments(self):
        return [instrument.get_name() for instrument in self.instruments if isinstance(instrument, StringedInstrument)]

    def list_percussion_instruments(self):
        return [instrument.get_name() for instrument in self.instruments if
                isinstance(instrument, PercussionInstrument)]

chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuso")
drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")
orchestra = Orchestra()
orchestra.add_instruments(chello)
orchestra.add_instruments(maracas)
orchestra.add_instruments(violin)
orchestra.add_instruments(drums)

print("В оркестрe есть инструменты:", orchestra.list_instruments())
print("Струнные инструменты:", orchestra.list_stringed_instruments())
print("Ударные инструменты:",orchestra.list_percussion_instruments())

