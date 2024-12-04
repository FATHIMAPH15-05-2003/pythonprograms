arr1=[1,2,3,4,5,6,7,8]
arr2=[2,20,8,7,13,6,5]
counter=0
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        counter+=1
        if arr1[i]==arr2[j]:
            print(arr1[i])
            break

print("counter",counter)            