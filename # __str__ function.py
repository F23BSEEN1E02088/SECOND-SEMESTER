# __str__ function

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
        
p1 = person("Ali",20)
print(p1)