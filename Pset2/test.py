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
    word = list(secret_word)
    guessed = []
    for i in range(len(word)):
        if word in letters_guessed:
            guessed.append(word[i])
            i += 1
        else:
            i += 1

    print("Guess",guessed)
    print("Word",word)
    if guessed == word:
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
    word = list(secret_word)
    guessed = []
    for i in range(len(word)):
        if word[i].lower() in letters_guessed:
            guessed.append(word[i])
            i += 1
        else:
            guessed.append('_')
            i += 1    

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


secret_word = 'apple'
#letters_guessed = ['a', 'p', 'p', 'l', 'e']
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'g', 'v', 'l']
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

print("Secret word list:", list(secret_word))
print("Letter guessed:", letters_guessed)
#print(get_guessed_word(secret_word, letters_guessed))
print(is_word_guessed(secret_word, letters_guessed))

#print(get_available_letters(letters_guessed))