M=int(input("Enter the Month:"))
Y=int(input("Enter the Year:"))

if(M == 2 and (Y%400 == 0) or ((Y%100 != 0) and (Y%4 == 0))):
    print("The Month have 29 Days")
elif(M==2):
    print("The Month have 28 days")
elif(M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12):
    print("The Month has 31 days")
else:
    print("The Month has 30 days")