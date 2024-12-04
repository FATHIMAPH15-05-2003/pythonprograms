source_word="CHICKEN"
target_word="HEN" 

character_count={}
# for ch in source_word:
#     if ch in character_count:
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1
# print(character_count)        

# or
character_count={ch:source_word.count(ch) for ch in source_word}
is_kangaru_word=True
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]=-1
    else:
         is_kangaru_word=False
         break
print(is_kangaru_word)    