start=int(input("enter start"))#10
end=int(input("enter limit"))#50

if start<end:#10<50

    for num in range(start,end+1,1): 
        print(num)
else:
    for num in range(start,end-1,1):
        print(num)        