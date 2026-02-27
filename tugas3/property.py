class Person: 
  species = "Human"  # Class property    

  def __init__(self, name): 
        self.name = name  # Instance/object property 

p1 = Person("hakeem") 
p2 = Person("eng") 

print(p1.name) 
print(p2.name) 
 
class Person: 
  lastname = "" #sebelum dimofikasi 
  def __init__(self, name): 
    self.name = name 
 
p1 = Person("hakeem") 
p2 = Person("eng") 
 
Person.lastname = "purwodaddyh" #setelah dimodifikasi 
print(p1.lastname) 
print(p2.lastname) 
 
 
