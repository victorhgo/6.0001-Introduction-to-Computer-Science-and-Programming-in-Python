# Keyword arguments

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

printName("Victor","Correa", True)