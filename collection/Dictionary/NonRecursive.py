text="ABAACBCH"
character_count={ch:text.count(ch) for ch in text}
print(character_count)

#non_recursive
for k,v in character_count.items():
    if v==1:
       print(k) 

    #    or 
non_recursive_character={k for k,v in character_count.items() if v==1}
print(k)
