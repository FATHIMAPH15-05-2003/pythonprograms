#digit sum
number=int(input("enter number"))

total=0
while(number!=0):#18,1
    digit=number%10#18%10=8 1%10=1
    total=total+digit#8+0 9+0=9
    number=number//10#18//10=1 1//10=1
print(total)    
