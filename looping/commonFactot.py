number1=int(input("enter number"))#6....[1,2,3,6]
number2=int(input("enter number"))#8....[1,2,4,8]


for i in range(1,number1):
    if number1%i==0 and number2%i==0:
        print(i)
