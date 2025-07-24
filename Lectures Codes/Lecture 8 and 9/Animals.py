import random

class Animal(object):
    def __init__(self, age): # Age initializes an Animal type
        self.age = age 
        self.name = None # name is a data attribute although an instance is not initialized with it as a parm
    
    def getAge(self): # Getter
        """ Returns the age of object type Animal """
        return self.age

    def getName(self): # Getter
        """ Returns the name of object type Anima """
        return self.name

    def setAge(self, newAge): # Setter
        """ Sets an age for object type Animal """
        self.age = newAge
    
    def setName(self, newName=""): # Setter
        """ Sets a name for object type animal """
        self.name = newName
    
    def __str__(self): 
        """ Print method for object type Animal """
        return "Animal:"+str(self.name)+" : "+str(self.age)
    
class Cat(Animal): # Will inherits all attributes of Animal
    def speak(self): # Add new functionality (new method)
        print("Meow")

    def __str__(self): # Overrides __str__ from Animal
        return "cat:"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.setName(name)
        self.friends = []

    def getFriends(self):
        return self.friends
    
    def addFriend(self, friendName):
        if friendName not in self.friends:
            self.friends.append(friendName)
    
    def greet(self):
        print("Hey there")
    
    def ageDifference(self, other):
        difference = self.age - other.age
        print(abs(difference), "year difference")
    
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

class Student(Person): # Inherits Animal and Person attributes
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def __str__(self):
        return "Student Name: "+str(self.name)+" Age: "+str(self.age)+" Major: "+str(self.major)
    
    def changeMajor(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework to do")
        elif 0.25 <= r < 0.5:
            print("Oh my I need to sleep")
        elif 0.5 <= r < 0.75:
            print("I'm starving! I should eat")
        else:
            print("What a boring day, I will watch tv")

class Rabbit(Animal):
    tag = 1 # Class variable, shared across all instances, will be rabbit ID

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag # rID will receive class variable tag
        Rabbit.tag += 1

    def getRid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    
    def getParent1(self):
        return self.parent1
    
    def getParent2(self):
        return self.parent2
    
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parentSame = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parentOpposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parentSame or parentOpposite
    
    def __str__(self):
        return "rabbit:"+ self.getRid()

# Test Person subclass    
print("---- Person tests ----")
p1 = Person("Jack", 30)
p2 = Person("Jill", 25)
print(p1.getName())
print(p1.getAge())
print(p2.getName())
print(p2.getAge())
print(p1)
p1.greet()
p1.ageDifference(p2)
print("---- End Person Test ----")
# Test Student subclass

print("\n---- Student tests ----")
s1 = Student('Eliphas', 20, "CS")
s2 = Student('Anna', 18)
s3 = Student('Sugi', 21, "Medicine")
print(s1)
print(s2)
print(s3)
print(s1.getName(),"says:", end=" ")
s1.speak()
print(s2.getName(),"says:", end=" ")
s2.speak()
print(s3.getName(), "says: ", end=" ")
s3.speak()
print("---- End Student Test ----")

# Test Rabbit subclass

print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.getParent1())
print("r1 parent2:", r1.getParent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.getParent1())
print("r4 parent2:", r4.getParent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.getParent1())
print("r5 parent2:", r5.getParent2())
print("r6 parent1:", r6.getParent1())
print("r6 parent2:", r6.getParent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)
