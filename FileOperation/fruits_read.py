f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\fruits.txt")


fruits=[]
for line in f:
    print(line)
    fruits.append(line.rstrip("\n"))
print(fruits)    