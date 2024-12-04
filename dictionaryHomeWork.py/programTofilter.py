original_dictionary={'mango':65,'orange':45,'grape':75}

filtered_dictionary={key:value for key,value in original_dictionary.items()if value>50}

print(filtered_dictionary)