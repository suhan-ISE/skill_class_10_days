from abc import ABC, abstractmethod
class Greet(ABC):
    def __init__(self):
        pass
    
class English(Greet):
    def say_hello(self):
        return "Hello!!"
    
g = English()
print(g.say_hello())



class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    def move(self):
        return "moving"
    
class Dog(Animal):
    def make_sound(self):
        return "barks"
    
class Cat(Animal):
    def make_sound(self):
        return "Meowwww"
    
dog = Dog()
print(dog.make_sound())
print(dog.move())

cat = Cat()
print(cat.make_sound())
print(cat.move())
    