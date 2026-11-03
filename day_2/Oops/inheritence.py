class animal :
    def __init__(self,name):
        self.name = name 
    
    def info(self):
        print("Animal name :",self.name)
        
    
class dog(animal):
    def sound(self):
        print(self.name,"barks")
        

class cat(animal):
    def sound(self):
        print(self.name,"meow")
        
d = dog("roky")
c = cat("sheru")
d.info()
d.sound()
c.info()
c.sound()