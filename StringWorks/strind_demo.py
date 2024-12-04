# #capitalise
# #casefold
# #isdigit
# #isalpha
# #isalnum
# #startswith(str)
# #endswith(str)
# #vowels
# #split
# #strip
# #lstrip
# #rstrip



# text="hellopython"

# # print(text.capitalize())

# # print(text.casefold())

# # print(text.isalpha())

# # print(text.isalnum())

# # print(text.isdigit())

# # print(text.startswith("py"))

# # print(text.endswith("on"))

# # for ch in text:
# #     print(ch)
# text=text.casefold()
# for ch in text:
#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#         print(ch)





# text="hello world program"
#  #o => a
 
# new_text=text.replace("o","a") 
# print(new_text)





# text="python programming"
#   #01234567890123456
#   #string_object[start:end:step]

# print(text[0:6])  

# print(text[7:18])

# print(text[::2])



# text="hello"

# reversed_text=text[::-1]

# print(reversed_text)



# text="vipinkumar@gmail.com"
#      #01234567890123456789
# for i in range(0,10):
#     new_text=text.slice(0:10)
#     print(new_text)




# text="\n this is \n a line\n"

# new_text=text.lstrip("\n")
# print(new_text)



text="hellopython"
#     01234567890
substring=text[0:4]
reversed_substring=substring[::-1]
result=reversed_substring+text[4:]
print(result)
