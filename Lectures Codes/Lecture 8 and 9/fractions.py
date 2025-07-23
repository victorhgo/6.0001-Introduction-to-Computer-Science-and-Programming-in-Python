# EXAMPLE: simple class to represent fractions
# Try adding more built-in operations like multiply, divide - Done
# Try adding a reduce method to reduce the fraction (use gcd) - Will do

class Fraction(object):
    """
    A number represented as a fraction num / denom
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom

    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + " / " + str(self.denom)
    
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        if self.denom == other.denom:
            top = self.num + other.num
            bott = self.denom
        else:
            top = self.num*other.denom + self.denom*other.num
            bott = self.denom*other.denom

        return Fraction(top, bott)
    
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        if self.denom == other.denom:
            top = self.num - other.num
            bott = self.denom
        else:
            top = self.num*other.denom - self.denom*other.num
            bott = self.denom*other.denom

        return Fraction(top, bott)
    
    def __mul__(self, other):
        """Returns a new fraction representing the multiplication """
        top = self.num * other.num
        bott = self.denom * other.denom

        return Fraction(top, bott)
    
    def __truediv__(self, other):
        """ Returns a new fraction representing the division """
        top = self.num * other.denom
        bott = self.denom * other.num

        return Fraction(top, bott)
    
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)
    
    def reduce(self):
        """ Returns a new reduced fraction using GCD """
        pass

a = Fraction(1, 4)
b = Fraction(3, 4)

d = Fraction(2, 4)
e = Fraction(2, 3)

f = Fraction(50, 25)

c = a + b + d # c is a Fraction object
sub = a - b - e
mult = d * e
division = d / e
print("Multiplication:", mult)
print("Division:", division)
print("Inverse mult:", mult.inverse())
print("Sum:",c)
print("Dif:", sub)
print("Int to float:", float(c))
print("Fraction int to float:", Fraction.__float__(c))
print("Float of Inverse fraction:", float(b.inverse()))

print("Reduce", f.reduce())
