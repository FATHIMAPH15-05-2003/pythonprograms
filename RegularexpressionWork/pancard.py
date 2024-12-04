#3 alpabets
#4th place alphbets[PCAFHT]
#1alphabets
# 4digit
# 1 alpabets

pancard_no=input("enter number")
from re import fullmatch
pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

if pancard_no==None:
    print("invalid")
else:
    print("valid")