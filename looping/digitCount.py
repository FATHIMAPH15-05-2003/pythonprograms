number=int(input("number"))
total=0

while(number!=0):
    digit=number%10
    number=number//10
    total=total+digit
print(total)   