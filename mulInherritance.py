class Animal:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} is barking")
class Dog:
    def __init__(self,owner):
        self.owner=owner
    def eat(self):
        print(f"{self.owner} has given food to eat")
class Lucy(Animal,Dog):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Dog.__init__(self,owner)
    def walk(self):
        print(f"{self.name} can walk")
bulu=Lucy("bulu","Dip")
bulu.bark()
bulu.walk()
bulu.eat()
