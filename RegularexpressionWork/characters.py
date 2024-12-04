text="I have 3 cars and 2 bikes"

patterns="\w"#predefined all alphanumeric a-zA-Z0-9
patterns="\d"#digot
patterns="\D"#exclude^0-9
from re import finditer
matcher=finditer=(patterns,text)

for obj in matcher:
    print(obj.start(),obj.group()) 