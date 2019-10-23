# Convert RGB to Vector.
def RGBtV(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    v1 = round(r/255, 3)
    v2 = round(g/255, 3)
    v3 = round(b/255, 3)
    val = "Vector({}, {}, {})".format(str(v1), str(v2), str(v3))
    return val

# Convert Vector to RGB.
def VtRGB(V1, V2, V3):
    R = int(V1*255)
    G = int(V2*255)
    B = int(V3*255)
    C = "RGB({}, {}, {})".format(R, G, B)
    return C
