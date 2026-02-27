class Person: 
    def __init__(self, name, age): 
        self.name = name     
        self.__age = age 
    def get_age(self):     
        return self.__age 
    def set_age(self, age):     
       if age > 0: 
        self.__age = age     
       else: 
        print("Age must be positive") 
p1 = Person("Tobias", 26) 
print(p1.get_age()) 
p1.set_age(27) 
print(p1.get_age()) 
 
class Outer: 
    def __init__(self): 
        self.name = "Outer Class" 
class Inner:     
    def __init__(self): 
        self.name = "Inner Class" 
    def display(self): 
      print("This is the inner class") 
outer = Outer() 
print(outer.name) 
 
class Outer: 
    def __init__(self):     self.name = "Emma" 
class Inner: 
    def __init__(self, outer): 
      self.outer = outer 
    def display(self): 
      print(f"Outer class name: {self.outer.name}") 
outer = Outer() 
inner = Inner(outer) 
inner.display() 
 
