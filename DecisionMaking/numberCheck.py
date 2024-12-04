#read a number

num=int(input("enter number"))

if num%15==0:

    print(f"fizzbuzz")

elif num%5==0:

    print(f"buzz") 

elif num%3==0:

    print(f"fizz")

else:
    print("invalid number")

   