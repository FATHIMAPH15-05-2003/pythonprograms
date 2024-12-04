number1=int(input("enter first number"))
number2=int(input("enter second number"))

min_num=number1 if number1<number2 else number2
gcd=1
for i in range(1,min_num+1):
    if number1%i==0 and number2%i==0:
        gcd=i
print(gcd)        
