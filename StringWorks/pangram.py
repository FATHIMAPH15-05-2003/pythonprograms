text="The quick brown for jumps over the lazy dog"
alphabets_series="abcdefghijklmnopqrstuvwxyz"
is_pangram=True
for ch in alphabets_series:
    if ch not in text:
        is_pangram=False
        break
print(is_pangram)    
        

    