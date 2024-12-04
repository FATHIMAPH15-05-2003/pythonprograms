text="aababbaaaaabab"
#    01234567899123

#(start,group)

from re import finditer

pattern="a{2}"
#pattern="a{1,3}"   minimum 1 maximum 3
matcher=finditer=(pattern,text)

for m in matcher:
    print(m.start(),m.group())