integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list = [] # <- Empty list

print("len(integers):", len(integers)) # <- Evaluates to 10
print("Integers[0]:", integers[0]) # <- Evaluates to 0
print("Integers[1] + 2:", integers[1] + 2) # <- Evaluates to 3

# Lists can contain other lists:

realNumber = [integers, 3.1415, [-2, -1, 0]]
print("realNumber[0]:", realNumber[0]) # <- Evaluates to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], another list
print("len(realNumber):", len(realNumber)) # <- Evaluates to 3

print("realNumber[3]:", realNumber[2]) # <- Evaluates to [-2, -1, 0]

# Changing values:

list1 = [1, 2, 3]
print("List1 before changing:", list1)

list1[1] = 9

print("List1 after changing:", list1)

# Iterating over list elements, to sum the first 9 integers:
total = 0
for i in range(len(integers)):
    total += integers[i]

print("Sum of all elements: ", total)

# A cleaner way to do it
total = 0
for i in integers:
    total += i

print("Sum of all elements: ", total)

# Appending elements to a list:
even = [2, 4, 6]
print("Even before append:", even)
even.append(8)
print("Even after append:", even)

# Mutating lists with operator +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # list3 = [1, 2, 3, 4, 5, 6]
print("List1:", list1, "List2:", list2)
print("List3:", list3)

list1.extend([7, 8]) # > Mutate list1 to [1, 2, 3, 7, 8]
print("List1 after extend:", list1)

# Mutating list with remove operator
list4 = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original list4: ", list4)
list4.remove(1) # >
print("Remove 1 from list:", list4) 
list4.remove(2) #
print("Remove 2 from  list:", list4)
del(list4[3])   #
print("Del list4[3]:", list4)
print("Pop list4:", list4.pop()) 
print("List after pop():", list4)

# Convert list to strings and back
string = "My name is Victor"
print(string)

print("string.split(s)", string.split('s'))
print("string.split( )", string.split(' ')) # Split into words

list5 = ['a', 'e', 'i', 'o']
print("List5:", list5)
print("list5 ''.join:", ''.join(list5))
print("list5 '_'.join:", '_'.join(list5))

# print("list(string):", list(string))
# newList = list(string)



# EXERCISE: Test yourself by predicting what the output is and 
#           what gets mutated then check with the Python Tutor
# No need for Python Tutor for now

cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool) # ['blue', 'green']
print(warm) # ['red', 'yellow', 'orange']

colors1 = [cool] # 
print(colors1) # [[['blue', 'green']]]
colors1.append(warm) # [[colors1], [warm]]
print('colors1 = ', colors1) # [['blue', 'green'],['red', 'yellow', 'orange']]

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2) # [['blue', 'green'],['red', 'yellow', 'orange']]

warm.remove('red') # ['yellow', 'orange']
print('colors1 = ', colors1) # [['blue', 'green'],['yellow', 'orange']]
print('colors2 =', colors2) # ['blue', 'green'],['red', 'yellow', 'orange']]

for e in colors1:
    print('e =', e) # e = [blue, green,], e = ['yellow', 'orange']

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print("e1::",e1) # e1 = blue, e1 = red, e1 = yellow, e1 = 'orange'
    else:
        print("e =", e) # e = [blue, green,], e = ['yellow', 'orange']


flat = cool + warm # ['blue', 'green'] + ['yellow', 'orange']
print('flat =', flat) # ['blue', 'green','yellow', 'orange']]

print(flat.sort()) # Modifies the original list, sorts in alphabetical order
print('flat.sort() =', flat) # ['blue', 'green', 'orange', 'yellow']

new_flat = sorted(flat, reverse = True) # Creates a new list called new_flat, sorted with reverse
print('flat =', flat) # ['blue', 'green', 'orange', 'yellow']
print('new_flat =', new_flat) # ['yellow', 'orange', 'green', 'blue']

cool[1] = 'black' # from ['blue', 'green'] to ['blue', 'black']
print(cool) # ['blue', 'black']
print(colors1) # [['blue', 'black'],['yellow', 'orange']]

print("Test type:", type(colors1))