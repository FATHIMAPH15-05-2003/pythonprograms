from re import finditer

f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\regexpFileWork\\socialMedia.txt")

for line in f:
    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)
    for obj in matcher:

        print(obj.group())
