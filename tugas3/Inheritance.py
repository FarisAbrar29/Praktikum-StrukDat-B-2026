class Person: #parent class   
    def __init__(self, fname, lname): 
        self.firstname = fname     
        self.lastname = lname 
    def printname(self): 
        print(self.firstname, self.lastname) 
x = Person("home", "less") 

class Student(Person): #child class  
    pass
x = Student("sakura", "mai")
x.printname() 

class Person:   
    def __init__(self, fname, lname): 
        self.firstname = fname     
        self.lastname = lname 
    def printname(self): 
        print(self.firstname, self.lastname) 
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) 
x = Student("terry", "bogard") 
x.printname() 

class Person: 
    def __init__(self, fname, lname): 
        self.firstname = fname 
        self.lastname = lname 
    def printname(self): 
        print(self.firstname, self.lastname) 
class Student(Person): 
    def __init__(self, fname, lname, year): 
        super().__init__(fname, lname) 
        self.graduationyear = year    
    def welcome(self): 
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
x = Student("jo", "pacheon", 2006) 
x.welcome() 

 
