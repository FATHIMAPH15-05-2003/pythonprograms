expenses=[100,200,300,400]
#          0   1    2   3
#one by one
for exp in expenses:
    print(exp)



#add one object
expenses[0]=500
print(expenses)



#total expenses
total=0
for exp in expenses:
    total+=exp
print(total)



# max_expenses
max_expenses=0
for exp in expenses:
    if exp>max_expenses:
        max_expenses=exp
print(max_expenses)       
    