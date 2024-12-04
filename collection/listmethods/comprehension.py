#program to print square list

arr=[1,2,3,4,5,6]
square=[]
for num in arr:
    sq=num**2
    square.append(sq)
print(square)



#cubes

cubes=[]
for num in arr:
    result=num**3
    cubes.append(result)
print(cubes)    

#syntax

# Reference=[return loop condition]

cubes=[num**3 for num in arr]
print(cubes)


add_five=[num+5 for num in arr]
print(add_five)



odd_num=[num for num in arr if num%2!=0]
print(odd_num)




