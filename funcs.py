import math

def min_int(a,b):
    if a < b:
   	    return a
    else:
        return b

def moy_int(l=[]):
    s = sum(l)
    n = float(len(l))
    moy = s/n
    return moy

def med_int(l=[]):
    n = len(l)
    m = n//2
    l.sort()
    if n < 1:
        return None
    elif n % 2 == 1 :
        return l[m]
    else:
        return ( l[m] + l[m-1] ) / 2.0