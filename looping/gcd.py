#hcf of two number(gcd)highest common factor...koduthitt ulla 2 numberile factorslee...valiya no ann gcd
num1=int(input("enter first number"))#16
num2=int(input("enter second number"))#24


gcd=1

min_num=num1 if num1<num2 else num2


for i in range(1,min_num):

    if num1%i==0 and num2%i==0:
        
        gdc=i
        
print(gcd)