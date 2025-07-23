# Lectures 8 and 9 - Object Oriented Programming and Python Classes and Inheritance

Object Oriented Programming concept and its representation in Python, data control, inheritance and subclasses.

## What is Object Oriented Programming

Everything in Python is an object (a basic date) and they have a certain type (int, float, list, etc). But every object has a data representation, or how Python represents the object behind the scene and whether this object is a primitive type or composite, and a object also has a set of procedures for interaction with the object. (Methods or functions)

An object is an **instance** of a type, like $2$ is an instance of an _int_, _"string"_ is an instance of a _string_. We can create new objects of some types as well manipulate them, and also **destroy** them by using _del_ for instance. Python system will reclaim destroyed or inaccessible objects in a process called **garbage collection**.

Since objects are a **data abstraction**, they capture:

- Internal data representation: what is the object and how is it represented, also how the object stores and manages its data.

- Interface to interact with the object thru methods (procedures/functions) and also defines behaviour but hides implementation.

**Data Abstraction** allow us to use objects without knowing exactly how they work internally. We can think of the following example, a type list of integers where:

```list = [2, 4, 6, 8]``` has a type _list_, we can access its elements by index for instance, where we use the index in methods to manipulate the list. But internally it's represented by a linked list of cells:

```[2 | *] -> [4 | *] -> [6 | *] -> [8 | NULL]``` - Where the pointer * points to the next index of the linked list. So in the above example each node holds a value (integer stored in the list) and a pointer to the next, a concept I've learned while studying C.

With this **data abstraction**, programmers can work with lists without worrying about how it works in the hardware level. This process of hiding internal details is known by **encapsulation**.

### Advantages of Object Oriented Programming

OOP bundle data into packages together with procedures that work on them through well-defined interfaces, facilitating the **divide and conquer** concept for software development, because we can implement and test behaviour for each class separately, increasing modularity and reducing complexity.

Like functions, **classes** make it easier to reutilize code, and since each class has a separate environment, there will be no collision on functions names for instance.

Inheritance is also another advantage of OOP because it allows subclasses to reuse (subclasses get access to the methods of superclass), modify (they can redefine methods) or extend (add new functions for instance) the behaviour defined in a superclass. This means that the subclass can use all the functionalities like they're created, or it can override how it works, adding new behaviour or changing existing ones. **Lecture 9**s will inheritance in Python.

### Creating and Using our own types with classes

We need to make a distinction between creating a class and using an instance of the class: (we will go deeper on this subject later on, but for now)

1. Creating a class:

- We need to define the class name
- We need to define its attributes

2. Using the class:

- We need to create new instances of objects
- Define what operations will be performed on the instances

The keyword _class_ is used to define a new type:

```py
class Coordinate(object):
    # Define attributes here
```

Where _Coordinate_ is the **name/type** and _object_ is the **class parent**. Similarly to defining functions, indent code to indicate which statements are part of the class definition. The _object_ will mean that _Coordinate_ is a Python object and inherits all its attributes, so:

- _Coordinate_ is a **subclass** of _object_ and
- _object_ is a **superclass** of _Coordinate_

### What are Attributes?

Attributes are all data and procedures that belong to a class, where we can think of _data attributes_ as other objects that make up the class. In the _Coordinate_ example, a coordinate is made up of two numbers (usually and x and y axis).

_Methods_ are the procedural attributes, for instance a function that only works with this class, it's also how we interact with the object. In the _Coordinate_ example, we can define a distance between two coordinate objects, which will have no meaning to a distance between two list objects for instance.

To create an instance of the object, we can use a special method called ```__init__``` to initialize some data attributes, so:

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x # Two data attributes for every Coordinate object
        self.y = y # <- /
```

Where _self_ is an parameter to refer to an instance of the class and x, y are data which initializes a _Coordinate_ object.

**Creating an instance of a class:**

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x # Two data attributes for every Coordinate object
        self.y = y # <- /

coord = Coordinate(3,4) # Creates a new object of type Coordinate and pass in 3 and 4 to the __init__

origin = Coordinate(0,0) # Creates a new object of type Coordinate and pass in 0 and 0 to the __init__

print("Coordinate(x ,y), x =", coord.x, ", y =", coord.y) # We need to use the dot (.) to access an attribute of instance coord
print("Origin(x,y), x =", origin.x, ", y =", origin.y)
```

Data attributes of an instance are called **instance variables**, we don't need to provide any argument for self because Python does this automatically.

### What is a Method?

Methods are the procedural attributes, like a **function that only works with this class**. Python always passes the object as the first argument, so the convention is to use _self_ as the name of the first argument of all methods.

The dot operator is used to access any attribute, data or method of an object.

**Defining a method for the _Coordinate_ class**

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x # Two data attributes for every Coordinate object
        self.y = y # <- /

    def distance(self, other): # other: another parameter to method
        x_diff_square = (self.x - other.x) ** 2
        y_diff_square = (self.y - other.y) ** 2

        return (x_diff_square + y_diff_square) ** 0.5

coord = Coordinate(3,4) # Creates a new object of type Coordinate and pass in 3 and 4 to the __init__

origin = Coordinate(0,0) # Creates a new object of type Coordinate and pass in 0 and 0 to the __init__

print("Coordinate(x ,y), x =", coord.x, ", y =", coord.y) # We need to use the dot (.) to access an attribute of instance coord
print("Origin(x,y), x =", origin.x, ", y =", origin.y)

# Using the class:

print(coord.distance(origin))

# It's equivalent to print(Coordinate.distance(coord, origin))
```

Where in ```print(coord.distance(origin))```, _coord_ is the object to call method on, _distance_ is the name of the method and _origin_ is the parameter to method _distance_ (_self_ not include because it's implied to be _coord_)

**Printing Representation of an Object**

```py
>>> coord = Coordinate(3,4)
>>> print(coord)
<__main__.Coordinate object at 0x1030fc6e0>
```

It's not informative by default, but we can define our own print method. Since Python calls the ```__str__``` method when used with _print_ on our class object, we can define:

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x # Two data attributes for every Coordinate object
        self.y = y # <- /

    def distance(self, other): # other: another parameter to method
        x_diff_square = (self.x - other.x) ** 2
        y_diff_square = (self.y - other.y) ** 2

        return (x_diff_square + y_diff_square) ** 0.5
    
    def __str__(self): # __str__ a special method
        return "("+str(self.x)+", "+str(self.y)+")" # Must return a string
```

It will now print:

```py
>>> coord = Coordinate(3,4)
>>> print(coord)
(3, 4) # Return of the __str__ method

>>> print(type(coord))
<class '__main__.Coordinate'> # Type of object coord is a class Coordinate

>>> print(Coordinate)
<class '__main__.Coordinate'> # a Coordinate is a class

>>> print(type(Coordinate))
<class 'type'> # a Coordinate class is a type of object
```

We can use _isinstance()_ to check if an object is a _Coordinate_:

```py
>>> print(isinstance(coord, Coordinate))
True
```

For **special operator** like +, -, ==, <, >, len(), print, and many others, we can override these to work with our class like we did with _print_ above, we just need to define them with double underscores before/after, like:

```py
__add__(self, other) -> self + other
__sub__(self, other) -> self - other
__eq__(self, other) -> self == other
__lt__(self, other) -> self < other
__len__(self) -> len(self)
__str__(self) -> print self
```
#### Fractions

In the example below, we will create a new type to represent a number as a fraction. So the internal representation will be two integers: **numerator** and **denominator**. The interface (_methods_ or _how to interact_ with Fraction objects) can be:

- add, subtract
- print representation, convert it to a float
- invert the fraction

```py
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom

    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):

        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom

    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
```

Adding a new method to multiply two fractions:

```py
def __mul__(self, other):
    """Returns a new fraction representing the multiplication """
    top = self.num * other.num
    bott = self.denom * other.denom
    return Fraction(top,bott)

d = Fraction(2, 4)
e = Fraction(2, 3)

# We can multiply two fractions by:
multiply = d * e
```

Adding a new method to divide two fractions:

```py
def __truediv__(self, other):
    """ Returns a new fraction representing the division """
    top = self.num * other.denom
    bott = self.denom * other.num
    return Fraction(top, bott)

d = Fraction(2, 4)
e = Fraction(2, 3)

# We can call the division method:
division = d / e
```

### Power of Object Oriented Programming

We can bundle together objects that share common attributes and procedures that operate on those attributes.

We can use abstraction to make a distinction between how to implement an object vs how to use the object.

We can build layers of object abstractions that inherit behaviours from other classes of objects.

We can create our own classes of objects on top of Python's basic classes.

## Python Classes and Inheritance

In this part we will go deeper on classes and also Inheritance concept

### Classes

When using classes we will have two different perspectives when writing the code: Implementing the Class and Using the Class

When **implementing** a new object type with a class, we need to **define** the class and its data attributes (what is the object) and methods (how to use the object). Class name is the type and class is defined generically (using _self_ to refer to some instance while defining the class). Class also defines data and methods common across all instances.

When **using** the new object type in the code being written we need to create instances of the object type and do operations with them. Instance is **one specific** object and data attribute values vary between instances. Instance also has the structure of the class.

Since we use OOP and classes of objects to **mimic real life** and group different objects part of the same type, data attributes can be the representation of the object with data, e.g: ```for a car: colour, brand```. ```For an animal: age, name.```. ```For a coordinate: x and y values```, and etc.

The **procedural attributes** are the behaviours, operations and **methods** we define for our objects. E.g: ```For a car: turn it on, open the doors...```, ```For a coordinate: find distance between two coordinates```, ```For an animal: make a sound```.

We can define a class Animal:

```py
class Animal(object):
    def __init__(self, age): # Age initializes an Animal type
        self.age = age 
        self.name = None # name is a data attribute although an instance is not initialized with it as a parm

myAnimal = Animal(3) # myAnimal instance is initialized to self.age in class definition
```

#### Getter and Setter methods
