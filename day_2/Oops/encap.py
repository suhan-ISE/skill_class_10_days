class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # privating the age
        
    def get_age(self):
        return self.__age # to get the private age 
    
p1 = person("suhan",20)
print(p1.name)
# print(p1.age) here age will be not feched because we have privated the age by double underscore .
print(p1.get_age())