#begin 10
#end50
#Print all numbers feom begin to end

begin=int(input("enter starting from limit"))
end=int(input("enter limit"))
# if begin>end:#50>10
#     begin,end=end,begin
i=begin#10

while(i<=end):

    if i%2==0:

         print(i)

    i+=1  



#correct answer:

reverse=True if begin>end else False
print(reverse)
i=begin
while(i<=end if reverse==False else i>=end):
    if(i%2==0):
        print(i)
    if reverse==False:
        i+=1
    else:
        i-=1


