#write a program to print a year is leapyear or not

year=int(input("enter year"))

if (year%100!=0 and year%4==0) or (year%100==0 and year%4==0):
    print("leap year")
else:    
    print("not leap year")#all not century year are leap year