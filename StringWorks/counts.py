#print vowel count
#print consonent

text="thiruvananthapuram"

v_count=0
c_count=0
vowel_sequence="a","e","i","o","U"


for ch in text:
    # if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    if ch in vowel_sequence:
        v_count=v_count+1
    else:
        c_count=c_count+1
print("vowels count=",v_count)
print("consonants count=",c_count)