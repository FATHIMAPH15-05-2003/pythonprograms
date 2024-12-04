# largets number among three number

# num1>num2 and num1>num3 print num1
# num2>num1 and num2>num3 print num2
# num3>num2 and num3>num1 print num3
# num1==num2 and num1==num3 print three numbers  are equal
num1=int(input("neter first number"))
num2=int(input('enter secondnumber'))
num3=int(input("enter third number"))

if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num1 and num2>num3:
    print("num2 is lqrgets")
elif num3>num1 and num3>num2:
    print("num3 ids largest")
elif num1==num2 and num1==num3:
    print("three's are equal")

