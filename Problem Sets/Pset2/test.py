# test function implementation individually 
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    i = 0
    guessed = []

    for i in range(len(list(secret_word))):
        if list(secret_word)[i] in letters_guessed:
            guessed.append(list(secret_word)[i])
            i += 1
        else:
            i +=1

    if guessed == list(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    guessed = []
    for i in range(len(list(secret_word))):
        if list(secret_word)[i] in letters_guessed:
            guessed.append(list(secret_word)[i])
            i += 1
        else:
            guessed.append('_')

    return ' '.join(guessed)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available = list('abcdefghijklmnopqrstuvwxyz')
    i = 0

    for i in range(len(letters_guessed)):
        if letters_guessed[i] in list(available):
            available.remove(letters_guessed[i])
            i += 1
        else:
            i += 1

    return ''.join(available)

def getScore(secret_word, letters_guessed, guesses):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    Returns the score based on the amount of unique letters x remaining guesses
    '''
    i = 0
    score = 0

    for i in range(len(letters_guessed)):
        if letters_guessed[i] in list(secret_word):
            score += 1
            i += 1
        else:
            i += 1
    
    return score * guesses

# More helpers to get rid of if-else nested:

def warn_duplicateLetter(warnings):
    '''
    '''
    warnings -= 1
    print("Oops! You've already guessed that letter. You have", warnings, "warnings left")
    return warnings

def duplicateLetter(guess):
    '''
    '''
    guess -= 1
    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
    return guess

secret_word = 'apple'
#letters_guessed = ['a', 'p', 'p', 'l', 'e']
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'g', 'v', 'l']
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

print("Secret word list:", list(secret_word))
print("Letter guessed:", letters_guessed)
print(get_guessed_word(secret_word, letters_guessed))
#print(is_word_guessed(secret_word, letters_guessed))

#print(get_available_letters(letters_guessed))

