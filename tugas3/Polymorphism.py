class Car: 
    def __init__(self, brand, model): 
        self.brand = brand     
        self.model = model 
    def move(self):     
        print("Drive!") 
class Boat:   
    def __init__(self, brand, model): 
        self.brand = brand     
        self.model = model 
    def move(self):     
        print("Sail!") 
class Plane:   
    def __init__(self, brand, model): 
        self.brand = brand     
        self.model = model 
    def move(self):     
        print("Fly!") 
car1 = Car("Toyota", "innova")       #Create a Car object 
boat1 = Boat("Kapal", "lawutt") #Create a Boat object 
plane1 = Plane("Airways", "Qatar")     #Create a Plane object 
for x in (car1, boat1, plane1): 
    x.move()
 
