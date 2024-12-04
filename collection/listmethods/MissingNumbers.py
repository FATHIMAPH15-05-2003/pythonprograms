arr=[1,2,4,5]
#    0 1 2 3
arr.sort()
i=0
j=i+1
for i in range(0,len(arr)):
    result=arr[j]-arr[i]
    if result!=1:
        print(arr[i]+1,"is missing")
        break


