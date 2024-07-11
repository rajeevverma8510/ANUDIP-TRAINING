cp=float(input("Enter The cost prize: "))
sp=float(input("Enter The selling prize: "))
if(cp<0):
    print("Invalid")
elif(sp<0):
    print("Invalid")
else:
    if(sp>cp):
        print("PROFIT",sp-cp)
    elif(cp>sp):
        print("LOSS",cp-sp)
    else:
        print("NO PROFIT NO LOSS")
    