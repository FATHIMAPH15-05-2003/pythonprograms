#date:01/1/31

pattern="(0?[0-9]/1[0-9]/3[0-1])"
from re import fullmatch
date=input("enter number")
pattern="(0?[0-9]/1[0-9]/3[0-1])"

matcher=fullmatch(pattern,date)

if date==None:
    print("invalid")
else:
    print('valid')