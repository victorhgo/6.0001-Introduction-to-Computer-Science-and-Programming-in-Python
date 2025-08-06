# Problem Set 4B
# Name: Victor Correa
# Time Spent: 4h26min

from string import ascii_lowercase, ascii_uppercase

### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from", file_name,'...')
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []

    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])

    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()

    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        """
        validWords = self.valid_words
        return validWords

    def build_shift_dict(self, shift):
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        """
        shiftedLetters = {}

        # Note: you may find the string​ ​module’s ​ascii_lowercase ​constant helpful here.
        lowerCase = ascii_lowercase

        # Lower case:
        for letter in range(len(lowerCase)):
            indexShifted = (letter + shift) % 26
            shiftedLetters[lowerCase[letter]] = lowerCase[indexShifted]

        # There's also an ascii_uppercase to help me:
        upperCase = ascii_uppercase

        # Upper case:
        for letter in range(len(upperCase)):
            indexShifted = (letter + shift) % 26
            shiftedLetters[upperCase[letter]] = upperCase[indexShifted]

        return shiftedLetters
    
    def apply_shift(self, shift):
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        """
        shiftDictionary = self.build_shift_dict(shift)
        shiftedText = ''

        for char in list(self.get_message_text()):
            if char in shiftDictionary:
                shiftedText += shiftDictionary[char]

            # Remember: spaces and punctuation should not be changed by the cipher. 
            else:
                shiftedText += char

        return shiftedText
    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        """
        return self.shift

    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        """
        encryptDictionary = self.encryption_dict
        return encryptDictionary

    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift: (build_shift_dic and apply_shift)      
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        """
        changeShift = shift

        self.build_shift_dict(changeShift)
        self.apply_shift(changeShift)

class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        # Hint: use the parent class constructor to make your code more 
        # concise. Take a look at Style Guide #7 if you are confused.
        super(CiphertextMessage, self).__init__(text)

        #self.message_text = text
        #self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        # What is the best shift for decrypting the message?
        bestShift = 0
        # valid words when decrypting the message:
        validWords = 0
        # best looking message based on words in words.txt
        bestDecryption = ''

        for shift in range(26):
            decryptedMessage = self.apply_shift(shift)
            # Hint1: String method split is useful
            words = decryptedMessage.split()
            count = 0
        
            # Check each word in the string if in words.txt (valid words)
            for word in words:
                # Hint2: helper function is_word(wordlist,word) is helpful here
                if is_word(self.get_valid_words(), word):
                    count += 1

            if count > validWords:
                validWords = count
                bestShift = shift
                bestDecryption = decryptedMessage

        return (bestShift, bestDecryption)


if __name__ == '__main__':

    # Test 1 - Encrypt method - PASS
    cypher1 = Message('Cypher is working I think...')

    test1 = cypher1.apply_shift(2)
    assert test1 == 'Earjgt ku yqtmkpi K vjkpm...'
    
    print("Test 1: Pass!!! Message:", test1)

    # Test 2 - PlaintextMessage - PASS
    plainText1 = PlaintextMessage('hello', 2)
    assert plainText1.get_message_text_encrypted() == 'jgnnq'

    print("Expected output: jgnnq")
    print("Test:", plainText1.get_message_text_encrypted())

    # Test 3 - CiphertextMessage - PASS
    ciphertext = CiphertextMessage('jgnnq')
    assert ciphertext.get_message_text() == 'jgnnq'

    print("Test object:", ciphertext.get_message_text())

    assert ciphertext.decrypt_message() == (24, 'hello')
    print('Test passed, result:', ciphertext.decrypt_message())


    # Test 5 - Decrypt a phrase - PASS
    cypher2 = Message('Decrypt this one now, haaa!!!')
    test2 = cypher2.apply_shift(5)
    print('test2:', test2)
    phrase = CiphertextMessage('Ijhwduy ymnx tsj stb, mfff!!!.')
    print("Decrypted test2: ", phrase.decrypt_message())

    """
    Test 6 - Story.txt - Final test - PASS

    Hint: The skeleton code contains a helper function get_story_string that returns 
        the encrypted version of the story as a string. Create a story object 
        using the story string and use decrypt_message to return the appropriate shift 
        value and unencrypted story.
    """
    story = CiphertextMessage(get_story_string())
    decryptedStory = story.decrypt_message()

    print("The best shift values for decrypting story is:", decryptedStory[0])
    print("Story decrypted:", decryptedStory[1])

    """ Best shift value used to decrypt the story: 12

    Story decrypted: Jack Florey is a mythical character created on the spur of a moment to help cover 
        an insufficiently planned hack. He has been registered for classes at MIT twice before, 
        but has reportedly never passed aclass. It has been the tradition of the residents 
        of East Campus to become Jack Florey for a few nights each year to educate incoming 
        students in the ways, means, and ethics of hacking. """