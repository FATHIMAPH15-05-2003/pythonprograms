arr=[10,20,30,40,50]
# result={}
# for num in arr:
#     if num%2==0:
#        result[num**2]=num
# print(result)


# or

even_squares={num:num**2 for num in arr if num%2==0}
print(even_squares)