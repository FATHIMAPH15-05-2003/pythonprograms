from re import fullmatch
mobile_number=input("enter name")

pattern="(91)?[0-9]{10}"

#*....meaning(91)*..91 varam ,varand irikyam
#?...optional
#+...varannam


matcher=fullmatch(pattern,mobile_number)
if matcher==None:

    print("invalid")
else:
    print("valid")