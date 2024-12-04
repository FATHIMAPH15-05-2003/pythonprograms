# staring with KL
#2digit
#alphabets mininmun 1 and maximum 2
# 4 digit

from re import fullmatch
vehicle_registration=input("enter number")
pattern="(kL)[0-9]{2}[A-Z]{1,2}{0-9]{4}"

matcher=fullmatch(pattern,vehicle_registration)

if vehicle_registration==None:
    print("invalid")
else:
    print('valid')