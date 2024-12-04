def is_palindrome(lst):
    return lst==lst[::-1]

my_lst=[1,2,3,2,1]
if is_palindrome(my_lst):
    print("the list is palindrome")
else:
    print("the list is not palindrome")