from re import fullmatch

pattern="[a-z]+[a-z0-9]{5-63}@gmail.com"
gmail_id=input("enter gmail")
matcher=fullmatch(pattern,gmail_id)
print("invalid" if matcher==None else "valid")