arr=[1,2,3,4,5,6,7]

search_element=int(input("enter number"))
is_present=False
for i in range(0,len(arr)):
    if search_element==arr[i]:
        is_present=True
        break
print(is_present)    
        
