# #print all century year from 1800 to 2024
# year=int(input("enter year"))

for year in range(1800,2025,1):
    if year%100==0:
        print(year)      
