employee={"id":100,"name":"vipin","depatrment":"scirnce","salary":2500}

# #using get()
print(employee.get("salary"))


# # return all keys
for k in employee.keys():
   print(k)


  # OR

employee_keys=employee.keys()
print(employee_keys)   

# #fetch all values
for v in employee.values():
   print(employee)


# fetch key and values
for k,v in employee.items():
   print(k,v)   