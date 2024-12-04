#number=int(input("enter number"))
#digit_count=len(str(number))
#print(digit_count)

number=int(input("enter number"))#1534
# orginal=number #to check amstrong
digit_count=len(str(number))#4
total=0   
while(number!=0):
    digit=number%10#1534%10=4 153%10=3
    exponent=digit**digit_count#4**4 3**4
    total=total+exponent
    number=number//10
print(total)
# ams="number is amstrong" if orginal==total else "number is not amstrong"
# print(ams)

