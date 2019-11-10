'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name='', place=''):
    '''
    function1
    '''
    final_output = ''
    if user_name and place:
        final_output = 'Hello, ' + user_name + ', and welcome to ' + place
    elif user_name:
        final_output = 'Hello, ' + user_name + ', and welcome' + place
    elif place:
        final_output = 'Hello' + user_name + ' and welcome to ' + place
    else:
        final_output = 'Hello' + user_name + ' and welcome' + place
    return final_output

# Create a function called list_average()
# without using any libraries to do the maths for you
# (the point of this exercise is to practice interacting
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list



def list_average(argument1, avg_type="mean"):
    '''
    function2
    '''

    if avg_type == "median":
        argument1.sort()
        length = len(argument1)
        if argument1 == []:
            median = None
        if length % 2 == 0:
            median1 = argument1[length//2]
            median2 = argument1[(length//2) - 1]
            median = (median1 + median2)//2
        if length % 2 != 0:
            median = argument1[length//2]
        return median
    if avg_type == "mode":
        from collections import Counter
        dictionary = dict(Counter(argument1))
        maximum1 = max(dictionary, key=dictionary.get)
        argument1.reverse()
        dictionary = dict(Counter(argument1))
        maximum2 = max(dictionary, key=dictionary.get)
        if maximum1 == maximum2:
            answer = [maximum1]
        else:
            answer = [maximum1, maximum2]
        return answer
    if avg_type:
        if len(argument1) != 0:
            output = sum(argument1)/len(argument1)
        else:
            output = 0
        return output
