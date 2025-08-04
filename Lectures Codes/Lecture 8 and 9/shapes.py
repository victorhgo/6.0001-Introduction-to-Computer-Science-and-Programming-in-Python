# Define pi as a global variable
pi = 3.1415

class Shape(object):
    """ Abstract class Shape """
    def area(self):
        """ Assumes shape measurements as floats
            Return the area of the shape as a float"""
        pass

class Circle(Shape):
    """ Circle receives as measurement: radius """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius*self.radius)

class Rectangle(Shape):
    """ Rectangle receives as measurement: width and height """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """ Rectangle's Area: width * height """
        return self.width * self.height

class Triangle(Shape):
    """ Triangle receives as measurement: base and height"""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        """ Triangle's area: 1/2 * base * height"""
        return (self.base * self.height) * (0.5)

# Create some objects to test the area() method
circle = Circle(radius=2)
rectangle = Rectangle(width=4, height=5)
triangle = Triangle(base=3, height=6)

assert round(circle.area(), 2) == round(pi * 2 * 2, 2)
assert rectangle.area() == 20
assert triangle.area() == 9

# Next step: Using Polymorphism to create a list of shapes:
shapes = [
    Circle(2),
    Rectangle(4, 5),
    Triangle(3, 6)
]

# Test the list:
assert round(shapes[0].area(),2) == round(pi * 2 * 2, 2)
assert shapes[1].area() == 20
assert shapes[2].area() == 9

# Test output from list
for shape in shapes:
    print(f"Area: {round(shape.area(),2)}")
