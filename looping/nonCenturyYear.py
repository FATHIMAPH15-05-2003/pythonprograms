
#non century year
for year in range(1800,2025,1):
    if year%100!=0 and year%4==0:
        print(year)        
