text="I have 3 cars and 2 bikes"
#     0123456789012345678901234

# patterns="[abc]"#either a or b or c
patterns="[a-zA-Z0-9]"#chck all alphbets and digit
# patterns="[^ak]"#eclude a and 
from re import finditer

matcher=finditer=(patterns,text)

for obj in matcher:
    print(obj.start(),"==>",obj.group())