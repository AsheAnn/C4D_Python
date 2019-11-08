time = input("Time(sec):  \n>")
frame = input("Frame(frames):  \n>")

def rendertime(time, frame):
    t = float(time)
    f = float(frame)
    a = t * f
    if a == 86400:
        rt = a/3600/24
        print round(rt, 2), 'Day'
    elif a > 86400:
        rt = a/3600/24
        print round(rt, 2), 'Days'
    elif 86400 > a > 3600:
        rt = a/3600
        print round(rt, 2), 'Hours' 
    else:
        rt = a/3600
        print round(rt, 2), 'Hour'    

rendertime(time, frame)  
