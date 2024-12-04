year_path="C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\year.txt"

century_year_Path="C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\centuryYear.txt"

leap_year_path="C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\leapYear.txt"

f_read=open(year_path,"r")
f_century=open(century_year_Path,"w")
f_leap=open(leap_year_path,"w")


def is_century_year(year):
    return True if year%100 ==0 else False

def is_leap_year(year):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        return True
    else:
        return False
    
for year in f_read:
    year=int(year)
    if is_century_year(year):
        f_century.write(str(year)+"\n" )   
    if is_leap_year(year):
        f_leap.write(str(year)+"\n")    

    

f_read.close() 
f_century.close() 
f_leap.close()  
