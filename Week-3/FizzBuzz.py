'''FizzBuzz exercice'''
first_value = 0
for first_value in range(101):
    if first_value%3 == 0 and first_value%5 == 0:
        print('fizz-buzz')
    elif first_value%3 == 0 and first_value != 0:
        print('fizz')
    elif first_value%3 != 0 and first_value%5 == 0:
        print('buzz')
    else:
        print(first_value)
