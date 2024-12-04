from re import findall
f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\regexpFileWork\\urls.txt")
content=f.read()
pattern="https?://[\w\S./]+"
url=findall(pattern,content)


for urls in url:
    print(urls)