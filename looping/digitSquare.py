#digit_square
num=int(input("enter number"))
total=0
while(num!=0):#145!=0 14!=0 1!=0
    digit=num%10#145%10=5 14%10=4 1%
    digit_square=digit**2#5**2 4**2
    total=total+digit_square#0+25 25+16
    num=num//10#145//10=14 14//10=1
print(total)    


