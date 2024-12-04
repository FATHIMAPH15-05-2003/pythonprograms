num=int(input("enter number"))
is_perfect=False
sum=0
for i in range(1,num):
    if num%i==0:
        is_perfect=True
        break
print(is_perfect)    
        
        