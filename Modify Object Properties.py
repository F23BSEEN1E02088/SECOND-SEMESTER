class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def func(self):
        print("Hello my name is" + self.name)
        
p1 = person("ali",20)
p1.age = 40
print(p1.age)
