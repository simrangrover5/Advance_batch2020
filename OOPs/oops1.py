
from time import sleep

class Student:
    total = 0
    def __init__(self,name,age,phno):
        self.name = name
        self.age = age
        self.phno = phno
        Student.total += 1
    def get_attr(self):
        for attr,value in self.__dict__.items():
            print("Attribute : ",attr,"Value : ",value)
            
    def get_total(self):
        print("\n The total number of students are : ",Student.total)
        
    def __repr__(self):
        return f"{self.name}"
    
    def __str__(self):
        return f"{self.name}"
    
    def __del__(self):
        print("Deleting : ",id(self))
        sleep(3)
        del self
        
s1 = Student("shahid",20,987564321)  #__init__ will be called
s2 = Student("Sahil",22,9876543210)
s3 = Student("Komal",24,9876543210)

s1.get_attr()
s2.get_attr()
s3.get_attr()

del s1
del s2
del s3

print(s1)
print(s2)
print(s3)
