# second largest
num1=int(input("neter first number"))
num2=int(input('enter secondnumber'))
num3=int(input("enter third number"))

if num1>num2 and num1>num3:
    if num2>num3:
      print("num2 is second largest")
    else:
        print("num3 is secoond largest")
elif num2>num1 and num2>num3:
    if num1>num3:
        print("num1 is second largets")
    else:
        print("num3 is second largest")
elif num3>num1 and num3>num2:
    if num1>num2:
        print("num1 is second largest")
    else:
        print("num2 is second largest")

# elif num1==num2 and num1==num3:
#     print("three's are equal")


