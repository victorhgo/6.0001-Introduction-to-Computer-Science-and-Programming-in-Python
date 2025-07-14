# Cheerleader Robot - Revision
an_letters = "aefhilmnorsx"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm Level (1-10): "))

for char in word:
    if char.lower() in an_letters:
        print("Give me an " + char.upper() + "! " + char.upper())
    else:
        print("Give me a " + char.upper() + "! " + char.upper())

print("What does that spell?")
for i in range(times):
    print(word.upper(), "!!!")