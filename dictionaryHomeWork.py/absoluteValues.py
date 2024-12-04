my_dictionary={'a':-1,'b':2,'c':3,'d':-2}

abs_dictionary={key: abs(value)for key,value in my_dictionary.items()}
print(abs_dictionary)