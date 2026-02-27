class Calculator: 
  def add(self, a, b): 
    return a + b 
  def multiply(self, a, b): 
    return a * b 
  
calc = Calculator() 
print(calc.add(2, 10)) 
print(calc.multiply(2, 10)) 
 

#__str__ method
class Person:   
    def __init__(self, name, age): 
        self.name = name     
        self.age = age 
    def __str__(self): 
        return f"{self.name} ({self.age})"  
       
p1 = Person("masasi Kisihimoto", 75) 
print(p1) 
 
 
