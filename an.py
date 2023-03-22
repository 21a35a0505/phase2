from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def barking(self):
        pass
    @abstractmethod
    def food_preference(self):
        pass
    @abstractmethod
    def color(self):
        pass
class Dog(Animal):
    def barking(self):
        print("dog style")
    def food_preference(self):
        print("veg or non veg anything")
    def color(self):
        print("any color avilable")

class Cow(Animal):
    def barking(self):
        print("Cow style")
    def food_preference(self):
        print("veg only")
    def color(self):
        print("Combinaton's avilable")
class Buffalo(Animal):
    def barking(self):
        print("dog style")
    def food_preference(self):
        print("veg only")
    def color(self):
        print("black")
class An:
    dog=Dog()
    cow=Cow()
    buffalo=Buffalo()
    dog.barking()
    cow.barking()
    buffalo.barking()
