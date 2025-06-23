
# --------------> CLASSES AND OBJECT <-----------------
# classes:a class is like object constructor or blue print for creating object
# object : every thing in python is an object

# creating class:

#   create a class we need the key word Class followed by the name and colon.class name should be camelcase
class person:
    pass
print(person)

# creating object:
p=person()
print(p)

# class constructor
#   the class without a constructor is not really usefull in real application
#   so to make useful we use _init_(self,...) constructor function,this constructor has self parameter which is reference to current instance of class

class Person:# -------------------------> class
    def __init__(self,name):#      |
        self.name=name      #      |----> class constructor
                            #      |
p=Person("arpit")#----------------------> object
print(p.name)
print(p)

# more parameter and inordered parameter
class Person:
    def __init__(self,fname,lname,age,country):
        self.firstname=fname
        self.lastname=lname
        self.country=country
        self.Age=age    
                           
p=Person("arpit","mishra","india",22)
print(p.firstname)
print(p.lastname)
print(p.Age)
print(p.country)

# object method : the method are function which belongs to the object
class Person:
    def __init__(self,fname,lname,age,country):
        self.firstname=fname
        self.lastname=lname
        self.country=country
        self.Age=age    
    def PersonInfo(self):
        return f"{self.firstname} {self.lastname}"                      
p=Person("arpit","mishra","india",22)
print(p.PersonInfo())

# object default method
class Person:
    def __init__(self,fname="arpit",lname="mishra",age=22,country="india"):
        self.firstname=fname
        self.lastname=lname
        self.country=country
        self.Age=age

    def PersonInfo(self):
        return f"{self.firstname} {self.lastname}, i am {self.Age} years old,i am from {self.country}"                      
p1=Person()
print(p1.PersonInfo())
p2=Person("ratikanta","jena",22,"bharat")
print(p2.PersonInfo())

# method to modify class default value
class Person:
    def __init__(self,fname="arpit",lname="mishra",age=22,country="india"):
        self.firstname=fname
        self.lastname=lname
        self.country=country
        self.Age=age
        self.skills=[]

    def PersonInfo(self):
        return f"{self.firstname} {self.lastname}, i am {self.Age} years old,i am from {self.country}"  
    def PersonSkill(self,skill):
        self.skills.append(skill) 
# create person objects                   
p1=Person()
print(p1.PersonInfo())
# add skills to p1
p1.PersonSkill("html")
p1.PersonSkill("css")
p1.PersonSkill("pyscript")
# print p1 skills
print(p1.skills)
# create person p2
p2=Person("ratikanta","jena",22,"bharat")
print(p2.PersonInfo())
print(p1.skills)

print(p2.skills)

p2.PersonSkill("java")
p2.PersonSkill("react")
p2.PersonSkill("javacript")

print(p2.skills)

# inheritance 
class Person:
    def __init__(self,fname="arpit",lname="mishra",age=220,country="indiaa"):
        self.firstname=fname
        self.lastname=lname
        self.country=country
        self.Age=age
        self.skills=[]

    def PersonInfo(self):
        return f"{self.firstname} {self.lastname}, i am {self.Age} years old,i am from {self.country}"  
    def PersonSkill(self,skill):
        self.skills.append(skill) 

class Student(Person):
    pass
s1=Student("arpit","india",22)
s2=Student("rahul","bharat",24)
print(s1.PersonInfo())
s1.PersonSkill("html")
s1.PersonSkill("css")
s1.PersonSkill("pyscript")
print(s1.skills)

s2.PersonSkill("java")
s2.PersonSkill("react")
s2.PersonSkill("javacript")
print(s2.skills)

# overriding parent method
class Person:
    def __init__(self,fname="arpit",lname="mishra",age=220,country="indiaa"):
        self.firstname=fname
        self.lastname=lname
        self.Age=age
        self.country=country
        
        self.skills=[]

    def PersonInfo(self):
        return f"{self.firstname} {self.lastname}, i am {self.Age} years old,i am from {self.country}"  
    def PersonSkill(self,skill):
        self.skills.append(skill) 

class Student(Person):
     def __init__(self,fname="arpit",lname="mishra",age=220,country="india",gender="male"):
         self.gender=gender
         super().__init__(fname,lname,age,country)
     def PersonInfo(self):
         gender="he" if self.gender =="male" else "she"
         return f"{self.firstname} {self.lastname} is {self.Age} years old.{gender} lives in {self.country}"
     
s1=Student("arpit","mishra",22,"india","male")
s2=Student("priyanka","panigrahi",22,"bharat","female")
print(s1.PersonInfo())

s1.PersonSkill("html")
s1.PersonSkill("css")
s1.PersonSkill("pyscript")
print(s1.skills)
print(s2.PersonInfo())
s2.PersonSkill("java")
s2.PersonSkill("react")
s2.PersonSkill("javacript")
print(s2.skills)