# user_input=input("enter brackets")

# symbol_dictionary={
#     "[":"]",
#     "{":"}",
#     "(":")"

# }
# symbol_stack=[]
# top=-1
# is_valid=True

# for symbol in user_input:
#     if symbol in symbol_dictionary:
#         top=+1
#         symbol_stack.append(symbol)
#     elif top==-1:
#        is_valid=False
#     elif symbol == symbol_dictionary.get(symbol_stack[top]):
#         top=-1
#         symbol_stack.pop()
#     else:
#         is_valid=False
# if len(symbol_stack)==0 and is_valid:
#     print("valid")
# else:
#     print("not valid")        

    
list1=["orange","onion","apple"]
list2=[100,200]

merge_lst={list1:list2 for item in list1}
print(merge_lst)