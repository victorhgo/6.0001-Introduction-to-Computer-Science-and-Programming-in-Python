# Problem Set 2, hangman.py
# Name: Victor Correa
# Collaborators: Victor Correa
# Time spent: 3h47min

# Finished part 1. Note:
# I have decided to not progress further to part 2

# Hangman Game
import random

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


def guessedWord(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    Returns True if all the letters of secret_word are in letters_guessed;
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


def getGuessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    i = 0
    guessed = []

    for i in range(len(list(secret_word))):
        if list(secret_word)[i] in letters_guessed:
            guessed.append(list(secret_word)[i])
            i += 1
        else:
            guessed.append('_')

    return ' '.join(guessed)


def availableLetters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
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
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    Returns the score based on the amount of unique letters x remaining guesses
    """
    i = 0
    score = 0
    word = list(secret_word)

    for i in range(len(letters_guessed)):
        if letters_guessed[i] in word:
            score += 1
            i += 1
        else:
            i += 1
    
    return score * guesses


def warn_duplicateLetter(warnings):
    """
    warnings: integer, warnings in the game. 
        When user inputs a letter that was already entered,
    Returns warning
    """
    warnings -= 1
    print("Oops! You've already guessed that letter. You have", warnings, "warnings left")
    return warnings


def duplicateLetter(guess):
    """
    guess: integer, guesses in the game
        When user inputs a letter that was already entered but no more warnings left,
    Returns guess
    """
    guess -= 1
    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
    return guess


def correctGuess(letter, letters_guessed):
    """
    letter: a letter entered by the user
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    secred_word: string, the word the user is guessing; assumes all letters are
      lowercase

    Validates if guess was entered correctly
    """
    letters_guessed.append(letter)
    print("Good guess:", getGuessed(secret_word, letters_guessed))


def incorrectGuess(letter, letters_guessed):
    """
    letter: a letter entered by the user
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase

    Validates if guess was not entered correctly
    """
    letters_guessed.append(letter)
    print("Oops! That letter is not in my word:", getGuessed(secret_word, letters_guessed))


def invalidInput(warnings, guess):
    """
    warnings: integer, all available warnings that user currently have
    guess: integer, all available guesses that user currently have

    Returns warning and guess based on the conditions
    """
    if warnings > 0:
        warnings -= 1
        print("Oops, this is not a valid letter. You have", warnings, " warnings left")
    else:
        guess -=1
        print("You have no warnings left so you lose one guess")
    
    return warnings, guess


def gameResult(secret_word, letters_guessed, guess):
    """
    Inputs: secret_word and letters_guessed as lists to compared them

    If the letters guessed are in the secret word, player wins, returning the game score based on
        guesses left x unique letters guessed in the word
    Otherwise, game is lost when guesses are equal to zero
    """
    if guessedWord(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", getScore(secret_word, letters_guessed, guess)) # Implement this
        exit(0)
    elif guess == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word)
        exit(0)     


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    """
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
        print("Available Letters: ", availableLetters(guessedLetters))
        letter = str.lower(input("Please guess a letter: "))

        if str.isalpha(letter):
            if letter in guessedLetters and len(letter) == 1:
                if warnings > 0:
                    warnings = warn_duplicateLetter(warnings)
                else: 
                    guess = duplicateLetter(guess)
                print(getGuessed(secret_word, guessedLetters))
            else:
                if letter in word:
                    correctGuess(letter, guessedLetters)
                else:
                    incorrectGuess(letter, guessedLetters)
                    guess -= 1
            print("--------------------")

        else:
            warnings, guess = invalidInput(warnings, guess)
            print("--------------------")

        gameResult(secret_word, guessedLetters, guess)

if __name__ == "__main__":
    secret_word = chooseWord(wordlist)
    hangman(secret_word)