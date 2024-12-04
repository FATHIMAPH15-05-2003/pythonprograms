number=int(input("enter number"))

is_Prime=True
for i in range(2,number):
    if number%10==0:
        is_Prime=False
        break
print(is_Prime)
