# def add_numbers(n1,n2):
#     return n1+n2
# print(add_numbers(3,4))



# def add_numbers(*args):# any number of arguments as a tuple

#     print(args)
# print(add_numbers(2,4,5))    



def product(*args):
    result=1
    for num in args:
        result=result*num
        return result


print(product(100,2,3))        
