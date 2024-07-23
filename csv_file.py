import csv
f=open("rko.csv",'w',newline="")
wo=csv.writer(f)
data=[["a","b","c","d"],[16,14,12,10],[26,24,22,20],[36,34,32,30]]
wo.writerows(data)
f=open("rko.csv",'r')
re=csv.reader(f)
li=list(re)
for i in li:
    print(i)
f.close()