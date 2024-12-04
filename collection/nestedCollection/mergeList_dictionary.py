list1=["orange","onion","apple","grape"]
#         0        1       2
list2=[100,200]
#       0    1
#       i

result={}
for i in range(0,len(list2)):
       lst_one_index_element=list1[i]
       lst_two_index_element=list2[i]

       result[lst_one_index_element]=lst_two_index_element
print(result)       

balance_elememt=list1[len(list2):]
for index,element in enumerate(balance_elememt):
       result[element]=index+1
print(result)       

