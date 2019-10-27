import math

def period(L, g):
    x = isinstance(L, (float, int))
    y = isinstance(g, (float, int))
    if x == True and y == True:
        if g != 0:
            if L>=0:
                T = 2*math.pi*(L/g)**0.5
            else:
                    raise ValueError
        else: 
            raise ValueError
    else:
        raise TypeError 
    return T