class Coordinate(object):
    def __init__(self, x, y):
        """ x and y can be int, floats """
        self.x = x # Two data attributes for every Coordinate object
        self.y = y # <- /
    
    def __str__(self): # __str__ a special method
        """ Prints the coordinate as (x, y)"""
        return "("+str(self.x)+", "+str(self.y)+")" # Must return a string
    
    def distance(self, other): # other: another parameter to method
        """ Returns the distance of two points """
        x_diff_square = (self.x - other.x) ** 2
        y_diff_square = (self.y - other.y) ** 2

        return (x_diff_square + y_diff_square) ** 0.5

coord = Coordinate(3,4) # Creates a new object of type Coordinate and pass in 3 and 4 to the __init__
coordinateA = Coordinate(1, 1)
coordinateB = Coordinate(2, 2)
origin = Coordinate(0,0) # Creates a new object of type Coordinate and pass in 0 and 0 to the __init__

print("Coordinate(x ,y), x =", coord.x, ", y =", coord.y) # We need to use the dot (.) to access an attribute of instance coord
print("Origin(x,y), x =", origin.x, ", y =", origin.y)
# Using the class:
print("Distance", coord.distance(origin))
print("CoordinateA(x, y) =", coordinateA)
print("CoordinateB(x, y) =", coordinateB)
print("Distance of Coordinate A and B:", coordinateA.distance(coordinateB))

# It's equivalent to print(Coordinate.distance(coord, origin))
