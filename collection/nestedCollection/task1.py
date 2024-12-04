list=[
     1,2,
     [3,4],
     [1,2,3,[10,2]],
     100
     ]
# list_object=[]
# for item in list:
#     if isinstance(item,list):
#         list_object.append(item)
# print(list_object)        


list_object=[item for item in list if isinstance(item,list)]
print(list_object)

print(max(list_object,key=len))
