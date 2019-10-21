a=0
for a in range(101):
    if a%3 == 0 and a%5 == 0:
        print ('fizz-buzz')
    elif a%3 == 0 and a%5 != 0:
        print ('fizz')
    elif a%3 != 0 and a%5 == 0:
        print ('buzz')
    else:
        print (a)
