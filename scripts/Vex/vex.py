# Program some Houdini's interpolation functions in python for C4d

import math


def lerp(v1, v2, f):
    z = (v2 - v1) * f + v1
    return z


 
def fit(val, omin, omax, nmin, nmax):
    s = float(val)
    a1 = float(omin)
    a2 = float(omax)
    b1 = float(nmin)
    b2 = float(nmax)
    if s <= a1:
        s = a1
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif s >= a2:
        s = a2
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif a2 > s > a1:
        s = s 
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)


def fit01(val, nmin, nmax):
    s = float(val)
    a1 = float(0)
    a2 = float(1)
    b1 = float(nmin)
    b2 = float(nmax)
    if s <= a1:
        s = a1
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif s >= a2:
        s = a2
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif a2 > s > a1:
        s = s 
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)


def fit10(val, nmin, nmax):
    s = float(val)
    a1 = float(1)
    a2 = float(0)
    b1 = float(nmin)
    b2 = float(nmax)
    if s <= a1:
        s = a1
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif s >= a2:
        s = a2
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif a2 > s > a1:
        s = s 
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)



def fit11(val, nmin, nmax):
    s = float(val)
    a1 = float(-1)
    a2 = float(1)
    b1 = float(nmin)
    b2 = float(nmax)
    if s <= a1:
        s = a1
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif s >= a2:
        s = a2
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
    elif a2 > s > a1:
        s = s 
        t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
        return round(t, 3)
 


# Return 'value' clamped between 'min' and 'max'. 
def clamp(val, min, max):
    s = float(val)
    min = float(min)
    max = float(max)
    if s <= min:
        return min
    elif s >= max:
        return max    
    elif max > s > min:
        return s    
    
# Return distance between 2 points.         
def distance(v1, v2):
    z = 0
    for i in range(0, 3):
        z += pow((v1[i] - v2[i]), 2)
    sum = round((math.sqrt(z)), 3)
    return sum
   

        
       
