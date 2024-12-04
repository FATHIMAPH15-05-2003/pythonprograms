text="aababbabab"
#     0123456789

#(start,group)

from re import finditer


matcher=finditer=("ab",text)

for m in matcher:
    print(m.start(),m.group())