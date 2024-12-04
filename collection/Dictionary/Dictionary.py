#store like=key:value pairs

#employee id=100 name=vipin department=science salary=2500

employee={"id":100,"name":"vipin","depatrment":"scirnce","salary":2500}

print(employee["name"])



#update
employee["salary"]=2700
print(employee)


#if expense>5 update slary as current_salary+1000 else current_salary+5000

if employee["experience"]>5:
    employee["salary"]+=10000
else:
    employee["salary"]+=5000
print(employee) 

