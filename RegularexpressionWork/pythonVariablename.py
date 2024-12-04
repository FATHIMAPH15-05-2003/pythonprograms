user_input=input("enter variable name")
from re import fullmatch

#starting with alphbets(uppercase,lowercase)
#any number of digits
patterns="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(patterns,user_input)

if matcher==None:
    print("invalid")
else:
    print("valid")