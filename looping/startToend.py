#print all numbers from start to end
#read

start=int(input("enter number"))
end=int(input("enter limit"))

for num in range(start,end+1,1):
    print(num)


#50 to 10
if start>end:
    for num in range(start,end-1,-1):
        print(num)