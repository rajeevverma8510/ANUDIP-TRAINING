s=float(input("Enter The Seconds "))
hour = 0;
min=0;
if(s>0):
    if(hour>=3600):
        hour = s//3600
        s = s%3600
    if(min>=60):
        min = s//60
        s = s%60
    sec = s
    print("HH:",hour,"MM:",min,"SS:",s)
else:
    print("INVALID TIME")