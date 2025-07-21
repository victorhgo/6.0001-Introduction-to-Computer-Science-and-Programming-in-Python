# Testing the implementations before moving to hangman.py
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
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

def correctGuess(letter, letters_guessed, secred_word):
    '''
    '''
    letters_guessed.append(letter)
    print("Good guess:", get_guessed_word(secred_word, letters_guessed))

def incorrectGuess(letter, letters_guessed, secred_word):
    '''
    '''
    letters_guessed.append(letter)
    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

def invalidInput(warnings, guess):
    '''
    '''
    if warnings > 0:
        warnings -= 1
        print("Oops, this is not a valid letter. You have", warnings, " warnings left")
    else:
        guess -=1
        print("You have no warnings left so you lose one guess")
    
    return warnings, guess

def gameResult(secret_word, letters_guessed, guess):
    '''
    '''
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", getScore(secret_word, letters_guessed, guess)) # Implement this
        exit(0)
    elif guess == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word)
        exit(0) 

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman
    '''
    guess = 6
    warnings = 3
    word = list(secret_word)
    guessedLetters = []
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is", len(secret_word),"letters long")
    print("You have", warnings, "warnings left")
    print("--------------------")

    while(1):
        print("You have", guess, "guesses left")
        print("Available Letters: ", get_available_letters(guessedLetters))
        letter = str.lower(input("Please guess a letter: "))

        # Final solution, with functions to validate each case separately
        if str.isalpha(letter) and len(letter) == 1:
            if letter in guessedLetters:
                if warnings > 0:
                    warnings = warn_duplicateLetter(warnings)
                else:
                    guess = duplicateLetter(guess)
                print(get_guessed_word(secret_word, guessedLetters))
            else:
                if letter in word:
                    correctGuess(letter, guessedLetters, secret_word)
                else:
                    incorrectGuess(letter, guessedLetters, secret_word)
                    guess -= 1
            print("--------------------")

        else:
            warnings, guess = invalidInput(warnings, guess)
            print("--------------------")

        gameResult(secret_word, guessedLetters, guess)

# Refactoring:
# From
# if str.isalpha(letter):
#     if letter in guessedLetters and warnings > 0:
#         warnings -= 1
#         print("Oops! You've already guessed that letter. You have", warnings, "warnings left")
#         print(get_guessed_word(secret_word, guessedLetters))
#         print("--------------------")
#     elif warnings == 0 :
#         guess -= 1
#         print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
#         print("--------------------")

#     else:
#         if letter in word:
#             guessedLetters.append(letter)
#             print("Good guess:", get_guessed_word(secret_word, guessedLetters))
#             print("----------------")
#         else:
#             guessedLetters.append(letter)
#             print("Oops! That letter is not in my word:", get_guessed_word(secret_word, guessedLetters))
#             print("----------------")
#             guess -= 1
# else:
#         if warnings != 0:
#             warnings -= 1
#             print("Oops, this is not a valid letter. You have", warnings, " warnings left")
#             print("--------------------")
#         else:
#             guess -= 1
#             print("You have no warnings left so you lose one guess")
#             print("--------------------")

# To:

# if str.isalpha(letter):
#     if letter in guessedLetters:
#         if warnings > 0:
#             warnings -= 1
#             print(f"Oops! You've already guessed that letter. You have {warnings} warnings left")
#         else:
#             guess -= 1
#             print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
#         print(get_guessed_word(secret_word, guessedLetters))
#     else:
#         guessedLetters.append(letter)
#         if letter in word:
#             print("Good guess:", get_guessed_word(secret_word, guessedLetters))
#         else:
#             print("Oops! That letter is not in my word:", get_guessed_word(secret_word, guessedLetters))
#             guess -= 1
#     print("--------------------")
# else:
#     if warnings > 0:
#         warnings -= 1
#         print(f"Oops, this is not a valid letter. You have {warnings} warnings left")
#     else:
#         guess -= 1
#         print("You have no warnings left so you lose one guess")
#     print("--------------------")

if __name__ == "__main__":
    #secret_word = chooseWord(wordlist)
    #secret_word = 'apple'
    secret_word = 'complicated'
    hangman(secret_word)