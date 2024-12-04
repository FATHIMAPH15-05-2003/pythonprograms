#def append(self)
#def pop(self)
#count
#def insert(self,index,object)
#rotate
#def index(self,object)
#def copy(self)
#def sort(self,reverse==false)


#append
colors=["red","green","blue","pink","yellow"]
# colors.append("yellow")
# print(colors)


#pop
colors.pop() 
print(colors)

#count
list=[10,20,30,20,50]
twenty_occurence=(list.count(20))
print(twenty_occurence)


#insert
colors.insert(2,"pink")
print(colors)
   

#rotate          ......k times k=1
num=[1,2,3,4,5]
k=1
for i in range(1,k+1):
    popped_element=num.pop()
    num.insert(0,popped_element)
print(num)


#index

red_index=colors.index("red")
print(red_index)


#copy

fatima_fvt_color=["red","orange","yellow"]
nazri_fvt_color=fatima_fvt_color
print(nazri_fvt_color)


#sort

lst=[1,2,4,6,3]
lst.sort()
print(lst)

#extend

color=['red','orange','pink']
fruit=['banana','apple','blueberry']
fruit.extend(color)
print(fruit)


#reverse

fruit.reverse()
print(fruit)


#syntax

# Reference=[return loop condition]

# condition ollathine==>filter
#,,         illathathine==>mapping
#group of object ne orimich==>reduce

arr=[2,3,4,5,6]
# cubes=[num**3 for num in arr]
# print(cubes)




add_five=[num+5 for num in arr]
print(add_five)



odd_num=[num for num in arr if num%2!=0]
print(odd_num)





