# Problem Set 4A
# Name: Victor Correa
# Time Spent: 4h20min

def getPermutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    >>> get_permutations('ab')
    ['ab', 'ba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1: # Base case
        return [sequence]

    permut = []

    for i in range(len(sequence)):
        currentChar = sequence[i] # Each character i in sequence
        # add the next char [:i] and next char to it [i+1:] (except current char)
        remainingChars = sequence[:i] + sequence[i+1:]

        # All permuts from the remaining string (called recursively)
        for j in getPermutations(remainingChars):
            permut.append(currentChar + j) # Appends each currentChars to the remaining string and appends to permut

    return permut

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', getPermutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print("Test1 (123)", getPermutations('123'))
    print("Test2 (Bat)", getPermutations('Bat'))
    print("Test3 (Dog)", getPermutations('Dog'))