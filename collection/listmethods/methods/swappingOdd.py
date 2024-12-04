arr=[100,200,300,400,500,600,700,800,900]
#     L                           R

left=1
right=len(arr)-1
if right%2==0:

    right-=1


while(left<=right):
    

    left+=2
    right+=2

print(arr)    