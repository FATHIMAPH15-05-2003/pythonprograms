from json import load

f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\words.txt",encoding="utf-8")
data=load(f)


#find number of countries
print(len(data))

all_country_names=[country.get("name")for country in data]
print(all_country_names)