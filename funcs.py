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

def ecart_int(l=[]):
    m = moy_int(l)
    n = len(l)
    e = 0.0
    for i in range(n):
        e += ((l[i]-m)**2)
    return e/n

def si_geo_int(l=[]):
    n = len(l)
    p = l[1]/l[0]
    for i in range (n-1):
        if (l[i+1]/l[i] != p):
            return False
    return True

def si_arith_int(l=[]):
    n = len(l)
    r = l[1]-l[0]
    for i in range (n-1):
        if (l[i+1]-l[i] != r):
            return False
    return True

def geo_int(n,l=[]):
    long = len(l)
    b = si_geo_int(l)
    if b == True :
        p = l[1]/l[0]
        s = [l[long-1]*p]
        for i in range (n-1):
            s.append(s[i]*p)
        return b, s
    else:
        return b, None

def arith_int(n,l=[]):
    long = len(l)
    b = si_arith_int(l)
    if b == True :
        r = l[1]-l[0]
        s = [l[long-1]+r]
        for i in range (n-1):
            s.append(s[i]+r)
        return b, s
    else:
        return b, None