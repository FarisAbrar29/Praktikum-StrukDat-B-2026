class Person:
    def __init__(self, name, age):
        # properti/atribut
        self.name = name
        self.age = age

# object dengan initial value p1
p1 = Person("terry", 20)
print(p1.name)
print(p1.age)

class Person: 
  pass 
 
#Mengatur properti object secara manual 
p1 = Person() 
p1.name = "eng" 
p1.age = 19
print(p1.name) 
print(p1.age) 

class Person: 
  def __init__(self, name, age=18): 
    self.name = name 
    self.age = age 

p1 = Person("surya") 
p2 = Person("marlong", 20) 

print(p1.name, p1.age)
print(p2.name, p2.age) 
 
 

 
