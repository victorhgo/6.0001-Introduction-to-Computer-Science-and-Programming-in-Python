# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
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
    permuts = []
    if len(sequence) == 1: # Base case
        permuts.append(sequence)
    else:
        i = 0
        for e in sequence:
            permuts.append(sequence[i + 1])
            i += 1
 
    return permuts


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


