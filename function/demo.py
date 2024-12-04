#create a function that take two parameter num1,num2 and return sum

# def sum(num1,num2):
#     result=num1+num2
#     print(result)
# sum(100,200)    
    



# def cube(num):
#     result=num**3
#     print(result)
# cube(4)        


# def sub(num1,num2):
#     result=num1-num2
#     print(result)
# sub(3,2)    


# def mul(num1,num2):
#     result=(num1*num2)
#     print(result)
# mul(3,4)    


# def div(num1,num2):
#     result=num1//num2
#     print(result)
# div(10,2)    


# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return(fact)

# result=factorial(3)
# print(result)



# #create a function num_chk return odd if num is odd else return even


# def num_chk(number):
#     if number%2==0:
#         return "even"

#     else:
#         return "odd"
# print(num_chk(10))


# #create a function max_two with two parameter num1,num2 return largest number

# def max_two(num1,num2):
#     return "num1" if num1>num2 else "num2"
# print(max_two(2,3))


# #create a function min_two with two parameter num1,num2 return smallest number


# def min_two(num1,num2):
#     return "num1" if num1<num2 else "num2"
# print(min_two(3,4))



# #create a function multiplication_table(number,n)print multiplication table of number till n


# def multiplication_table(number,n):
#     for i in range(1,n+1):
#         # if number>0:
#         #     n=number*i
#         #     print(n)
#         print(f"{i}*{number}={i*number}")

            
# multiplication_table(9,10)




# #create a function exponent with two parameter num1,n


# def expo(number,n):#n=exponent
#     return number**n
# print(expo(5,3))





# def smart_sub(num1,num2,reverse):
#     if reverse==True:
#         return num2-num1
#     else:
#         return num1-num2
# print(smart_sub(2,10,True))
    

# #create a function from strt to end

# start=int(input("enter start"))
# end=int(input("enter limit"))
# def random_numbers(start,end,step=2):#(10,20,2)
#     while(start<=end):
#         print(start)
#         start=start+step
# random_numbers(10,20)        
        


        #is_perfect_number

def prime(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    print(prime if is_prime==number else not prime)
             
