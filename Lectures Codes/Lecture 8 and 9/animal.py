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


# Creating an animal cat: instantiation creates an instance of an object:

cat = Animal(3)

# cat.age # Access data attribute, not recommended. Returns self.age
cat.setName("Ruby")
print("Name:Age -",cat)
print("Name:", cat.getName())
print("Age:", cat.getAge()) # Best to user getters and setters for data attribute

print("Cat2:")
cat2 = Animal(3)
cat2.setName()
print(cat2.getName())

# Argument passing:
print("Cat3:")
cat3 = Animal(2)
cat3.setName("Hugo")
print(cat3.getName())