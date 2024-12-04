arr=[100,200,300,400,500,600,700,800]

# odd_position_element=[]
# for i in range(0,len(arr)):
#     if i%2!=0:
#         odd_position_element.append(arr[i])
# print(odd_position_element)     




odd_position_element=[arr[i] for i in range(0,len,(arr)) if i%2!=0]
odd_position_element.reverse()
print(odd_position_element)
