from re import findall
f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\regexpFileWork\\data.txt")
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

all_dates=findall(pattern,content)

for m in all_dates:
    print(m)