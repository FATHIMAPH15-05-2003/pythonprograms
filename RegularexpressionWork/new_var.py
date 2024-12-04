#starting with alphabets from p-t
#in second place must be number that is\ by 3
#followed by  any number ,alphabets,@

from re import fullmatch
user_input=input("enter name")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"
matcher=fullmatch(pattern,user_input)
if matcher==None:

    print("invalid")
else:
    print("valid")