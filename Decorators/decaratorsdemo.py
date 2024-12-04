def smart_dec(fn):#fn=division(2,10)
    def wrapper(n1,n2):#n1=2,n2=10
        if n1<n2:#2<10  true
            (n1,n2)=(n2,n1) #2,10=10,2....n1=10,n2=2
        return fn(n1,n2)#diivision(10,2)
    return wrapper


def round_dec(fn):
    def wrapper(num1,num2):
        num1=round(num1)
        num2=round(num2)
        return fn(num1,num2)
    return wrapper  


@round_dec
@smart_dec
def smart_sub(num1,num2):

    return num1-num2


@round_dec
@smart_dec
def smart_div(num1,num2):
    return num1//num2  

print(smart_sub(10.8,2.6))
# print(smart_div(10,2 ))