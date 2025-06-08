class A:
    def some_method(self):
        print('Method A')
class B(A):
    def some_method(self):
        super().some_method()
        print('Method B')

x=B()
x.some_method()

class Shape:
    def __init__(self,shapename,**kwds):
        self.shapename=shapename
        super().__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self,color,**kwds):
        self.color=color
        super().__init__(**kwds)

cs=ColoredShape(color='red',shapename='circle')
print(cs.color)

class Engine:
    def start(self):
        print('Is running')

    def stop(self):
        print('Is stopped')

class Car:
    def __init__(self,brand):
        self.brand=brand
        self.engine=Engine()

    def start(self):
        print('The car started running')
        self.engine.start()

car=Car('toyota')
car.start()


class PersonalPC:
    def __init__(self,storage,disk,CPU):
        self.storage=storage
        self.disk=disk
        self.CPU=CPU

class Dekstop(PersonalPC):
    def __init__(self,storage,disk,CPU,monitor,keyboard,mouse,dimensions):
        super().__init__(storage,disk,CPU)
        self.monitor=monitor
        self.keyboard=keyboard
        self.mouse=mouse
        self.dimensions=dimensions

    def vyvod(self):
        print(f'Dekstop with {self.storage} GB, disk:{self.disk}, CPU:{self.CPU}, monitor:{self.monitor},'
              f'keyboard:{self.keyboard}')

class Laptop(PersonalPC):
    def __init__(self,storage,disk,CPU,dimensions,screen):
        super().__init__(storage,disk,CPU)
        self.dimensions=dimensions
        self.screen=screen

    def vyvod(self):
        print(f'Laptop with {self.storage} GB, disk:{self.disk}, CPU:{self.CPU}, dimensions:{self.dimensions},'
              f'screen size:{self.screen}')

l=Laptop()


