# Program some Houdini's interpolation functions in python for C4d

# Liner interpolation.
def lerp(v1, v2, f):
    z = (v2 - v1) * f + v1
    return z


# remap value in new range.
def fit(val, omin, omax, nmin, nmax):
    s = float(val)
    a1 = float(omin)
    a2 = float(omax)
    b1 = float(nmin)
    b2 = float(nmax)
    t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
    return round(t, 3)

# remap value in range (0, 1) to new range.
def fit01(val, nmin, nmax):
    s = float(val)
    a1 = float(0)
    a2 = float(1)
    b1 = float(nmin)
    b2 = float(nmax)
    t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
    return round(t, 3)

# remap value in range (1, 0) to new range.
def fit10(val, nmin, nmax):
    s = float(val)
    a1 = float(1)
    a2 = float(0)
    b1 = float(nmin)
    b2 = float(nmax)
    t = b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
    return round(t, 3)

# remap value in range (-1, 1) to new range.
def fit11(val, nmin, nmax):
    s = float(val)
    a1 = float(-1)
    a2 = float(1)
    b1 = float(nmin)
    b2 = float(nmax)
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
    
         

        
       
