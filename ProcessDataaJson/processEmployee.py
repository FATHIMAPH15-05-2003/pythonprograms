from json import load
f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\employee.json")

data=load(f)
print(data)    

for emp in data:
    print(emp)