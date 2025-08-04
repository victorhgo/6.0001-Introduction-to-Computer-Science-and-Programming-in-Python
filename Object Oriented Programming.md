# Simple test on Object Oriented Programming

**Time Spend: 2h36min**
**by Victor Correa**

    > Exercise codes at: /Lecture Codes/Lecture 8 and 9/

## Part 1: Fundamentals and Syntax of Object Oriented Programming
To Test my understanding of classes, objects, attributes, and methods:

**Exercise 1 – Class Basics (constructor and a method)**

Create a class Book with attributes title, author, and pages. Implement:

    A constructor
    A method getSummary() that returns a string like: "Title by Author, X pages"

Test the class like:

```py
book = Book("1984", "George Orwell", 328)
assert book.getSummary() == "1984 by George Orwell, 328 pages"
```

**Test Result:**
- [X] - Pass

**Exercise 2 – Encapsulation (Get and Set methods)**

Update Book so its attributes are private. Add:

    Getter and setter methods for each attribute.

    A method to check if the book is "long" (e.g., over 300 pages).

Test methods as:

```py
book = Book("Dune", "Frank Herbert", 412)

# Test getters
assert book.getTitle() == "Dune"
assert book.getAuthor() == "Frank Herbert"
assert book.getPages() == 412

# Test setters
book.setTitle("Dune Messiah")
book.setPages(256)
assert book.getTitle() == "Dune Messiah"
assert book.getPages() == 256

# Test logic
assert not book.isLong()  # 256 pages is not long
book.setPages(501)
assert book.isLong()
```

**Test Result:**
- [X] - Pass

## Part 2: Inheritance and Polymorphism

Further explore class hierarchies and method overriding.

**Exercise 3 – Inheritance**

Create a base class Vehicle with methods like start() and stop() then create the following derived classes:

    Car and Bike, each overriding the start() and stop() methods.

Test the class as:

```py
car = Car()
bike = Bike()

assert car.start() == "Car starting..."
assert car.stop() == "Car stopping..."

assert bike.start() == "Bike starting..."
assert bike.stop() == "Bike stopping..."
```
**Test Result:**
- [X] - Pass

**Exercise 4 – Polymorphism**

Moving further from Exercise 3, write a function operateVehicle(vehicle) that takes any subclass of Vehicle and calls start() and stop() on it.

Test with a Car and a Bike like:

```py
def operateVehicle(vehicle):
    return vehicle.start() + " " + vehicle.stop()

assert operateVehicle(Car()) == "Car starting... Car stopping..."
assert operateVehicle(Bike()) == "Bike starting... Bike stopping..."
```

**Test Result:**
- [X] - Pass

## Part 3: Abstraction and Interfaces

Let's use abstract classes (interfaces) to deal with some problems:

**Exercise 5 – Abstract Base Class**

Create an abstract class Shape with an abstract method area(). Implement:

    Circle, Rectangle, and Triangle classes that inherit from Shape and implement area().

```py
circle = Circle(radius=2)
rectangle = Rectangle(width=4, height=5)
triangle = Triangle(base=3, height=6)

# Area formulas
assert round(circle.area(), 2) == round(3.1415 * 2 * 2, 2)
assert rectangle.area() == 20
assert triangle.area() == 9
```

**Test Result:**
- [X] - Pass

## Part 4: Composition vs Inheritance

Working to model real-world problems with the correct OOP principles:

**Exercise 6 – Composition**

Design a Person class that has a Heart object and a Brain object.

    Heart and Brain have their own properties and methods (e.g., beat(), think()).

    Demonstrate how Person uses composition instead of inheritance.

Testing the class and objects as:

```py
person = Person()

# Make sure person delegates to components
assert person.heart.beat() == "Heart is beating"
assert person.brain.think() == "Thinking..."

# Or if methods are proxied:
assert person.heartbeat() == "Heart is beating"
assert person.thought() == "Thinking..."
```

**Test Result:**
- [X] - Pass

## Part 5: Still on Real-World Modeling

**Exercise 7 – Project: Library System**

Design a small library system with the following:

    Classes: Library, Book, Member

    Library can add/remove books and register members

    Member can borrow and return books

    Use inheritance if needed (e.g., different types of members)

    Apply encapsulation, composition, and possibly polymorphism

Test the library system as:

```py
library = Library()
book1 = Book("1984", "Orwell", 300)
book2 = Book("Brave New World", "Huxley", 288)
member = Member("Alice")

# Add books and register member
library.add_book(book1)
library.add_book(book2)
library.register_member(member)

# Borrow book
assert library.borrow_book("1984", "Alice") == "Book borrowed successfully"
assert not library.borrow_book("1984", "Alice")  # Already borrowed

# Return book
assert library.return_book("1984", "Alice") == "Book returned successfully"
assert library.borrow_book("1984", "Alice") == "Book borrowed successfully"
```
**Test Result:**
- [X] - Pass

## Final thoughts for this exercise set

After completing these exercises, answer the following questions:

**What are my strengths working with OOP:**

    Which concepts felt natural (e.g., inheritance, composition)?
    > Inheritance and Encapsulation felt natural while composition did not.


**What are my weaknesses (difficulty or uncertainty) working with OOP:**

    Did you struggle with abstraction or interfaces?
    > Abstraction (mainly with polymorphism and implementation) and Composition

**Conclusion**

    Working in this exercise set was a great opportunity to work further with OOP concepts and apply some deep thinking and learn new concepts.
    I'll be studying further this concepts and try to apply them on Problem Set 4.