# test function implementation individually 
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = chooseWord(wordlist)
    #hangman_with_hints(secret_word)


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

