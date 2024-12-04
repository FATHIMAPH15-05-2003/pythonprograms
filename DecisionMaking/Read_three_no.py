#read three numbers num1,num2,num3 print largest number amoung three numbers
a=int(input("enter value of num1:"))
b=int(input("enter value of num2:"))
c=int(input("enter value of num3:"))

# if a>b:
#     print("largest is",a)
#     print("largest is",b)
# elif b>c:
#     print("largest is",b)
#     print("largest is",c)
# elif a>c:
#     print("largest is",a)
#     print("largest is",c) 
# else:
#     print("largest number")  

if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
elif c>=a and c>=b:
        largest=c
        print("largest is",largest)
else:
    print(f"all are equal")        