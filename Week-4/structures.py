'''
structures.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list".
def first_and_last(the_list):
    '''
    function 1
    '''
    return [the_list[0], the_list[-1]]



# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    '''
    function2
    '''
    try:
        the_list = the_list[beginning:end]
        the_list.reverse()
        return the_list
    except:
        if end > beginning:
            raise ValueError

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    '''
    function3
    '''
    the_list.insert(index, index)
    the_list.insert(index, index)
    return the_list



# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    '''
    function4
    '''
    word = word.casefold()
    rev_word = reversed(word)
    return bool(list(word) == list(rev_word))

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    '''
    function5
    '''
    sentence.lower()
    sentence.split()
    sentence.replace(" ", "")
    sentence = sentence.casefold()
    rev_sentence = reversed(sentence)
    return bool(list(sentence) == list(rev_sentence))


# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    '''
    function6
    '''
    final_output = ''
    sentence1 = sentence1.split()
    sentence1 = sentence1[0].upper
    sentence2 = sentence2.split()
    sentence2 = sentence2[0].upper
    group = ['.', '!', '?']
    if sentence2[-1] in group and sentence1[-1] in group:
        final_output = str(sentence1) + ' ' + str(sentence2)
    if sentence2[-1] not in group and sentence1[-1] not in group:
        final_output = 'Your sentence must end with a full stop, question mark or an !'
    return final_output


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    '''
    function7
    '''
    return bool(key in dictionary.keys())

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    '''
    function8
    '''
    return bool(value in dictionary.values())

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''
    function9
    '''
    dictionary1.update(dictionary2)
    return dictionary1
