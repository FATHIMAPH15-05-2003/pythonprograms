st=set()#set
st={}#dictionary
st={10,20,30}#set
print(set)


#duplication not allowd
# set doesnt support indexing
# insertion is not preserved


#add
color={"red","green","orange"}
color.add("yellow")
print(color)



# sample
arr=[10,10,20,30,40,50]
st=set()
for num in arr:
    st.add(num)
print(st)    



#intersection
st1={10,20,30,40,50}
st2={10,20,30,40,60}
inter_section=st1.intersection(st2)
print(inter_section)


#union
union_set=st1.union(st2)
print(union_set)


#difference_set
differce_set=st1.difference(st2)
print(differce_set)

#remove

st1={10,20,30,40,50}
st1.remove(50)
print(st1)


#isSubset

st1={1,2,3}
st2={1,2,3,4,5}
print(st1.issubset(st2))


#isSuperset
print(st1.issuperset(st2))



#symmertric_difference
st1={1,2,3,10,20}
st2={1,2,3,4,5}
symmertric_difference=st1.symmetric_difference(st2)
print(symmertric_difference)


#update
st1.update(st2)
print(st1)

