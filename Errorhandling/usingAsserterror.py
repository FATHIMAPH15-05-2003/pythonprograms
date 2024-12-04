def poll(age):
    assert age>18,"invalid age"
    print("voted")
try:
    poll(19)
except Exception as e:
    print(e)    




def review(rating):
    assert rating>0,"too low"
    assert rating<0,"too high"
    print("rated")
try:
    review(4)    
except Exception as e:
    print(e)



def is_leap_year(year):
    if year%100!=0 and year%4==0 or year%100==0 and year%400==0:
        return True 
    else:
        return False 
    
def test_is_leap_year():
    assert is_leap_year(2024)==True,"non century year chk failed" 
    assert is_leap_year(2025)==False,"invalid noncentry chkmfailed" 
    assert is_leap_year(2000)==True,"centry leap year chk failed"
    assert is_leap_year(1900)==False,"invalid centru year chk failed"
    assert is_leap_year(-2024)==False,"invalid chk year failed"

try:
    test_is_leap_year()
    print("test case pass")

except Exception as e:
    print("test case failed",e)



def factorial(num):
  fact=1

for i in range(1,num+1):


