student={
         "suma":[10,20,30] ,
         "fathi":[13,25,30],
         "sura":[11,20,30] ,
         "arun":[15,20,34]



}

#index1 suma average mark
index=2
for i,element in enumerate(student):
      if i+1==index:
            print(element)

mark=student.get(element)
avg=sum(mark)/len(mark)
print(avg)