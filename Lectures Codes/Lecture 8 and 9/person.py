# Exercise 6

# First, the component classes:
class Heart:
    def beat(self):
        return "Heart is beating..."
    
class Brain:
    def think(self):
        return "Thinking..."


class Person(object):
    def __init__(self):
        self.heart = Heart()
        self.brain = Brain()

person = Person()

assert person.heart.beat() == "Heart is beating..."
assert person.brain.think() == "Thinking..."