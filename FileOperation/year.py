f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\year.txt","w")

for year in range(1800,2025):
    f.write(str(year)+"\n")

f.close()    