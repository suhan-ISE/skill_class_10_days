class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("drive!!",self.brand)
        
# car1 = Car("BMW","M5")
# print(car1.brand)
# print(car1.model)
# car1.move()

class Ship:
    def __init__(self,brand):
        self.brand = brand
        
    def move(self):
        print("deep dive",self.brand)
        
# ship1 = Ship("titanic")
# print(ship1.brand)
# ship1.move()

class Flight:
    def __init__(self,brand):
        self.brand = brand
        
    def move(self):
        print(self.brand,"fly!")
        
# fly1 = Flight("QATAR AIRWAYS")
# print(fly1.brand)
# fly1.fly()

car1 = Car("ford","mustang")
ship1 = Ship("titanic")
fly1 =  Flight("QATAR")

for x in (car1, fly1, ship1):
    x.move()
