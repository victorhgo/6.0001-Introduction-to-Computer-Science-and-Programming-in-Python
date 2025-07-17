# Map function
for i in map(abs,[-2, -3, -4]):
    print("Abs() applied:", i)

# Another example
list1 = [2, 28, 64, -128]
list2 = [3, 21, 58, -126]

for i in map(min, list1, list2):
    print("i: ", i)

# Lambda Expression
list = []

for i in map(lambda x, y : x * y, [1, 2, 3, 4],[4, 3, 2, 1]):
    list.append(i)

print("Lambda x, y : x * y:", list)

# Will do 1 * 4, 2 * 3, 3 * 2, 4 * 1


