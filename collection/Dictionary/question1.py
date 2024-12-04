arr=[10,20,30,40,2,4,6,7]

keys_squares={num:num**2 for num in arr}
print(keys_squares)



#even_squares
even_squares={num:num**2 for num in arr if num%2==0}
print(even_squares)