text="this is simple program this program count the word count this program is simple"
words=text.split(' ')
print(words)



words=["hai","hello","hai","hello","hai","is"]

# words_count={}
# for w in words_count:
#     if w in words:
#         words_count+=1
#     else:
#         words_count[w]=1
# print(words_count)        


word_count={w:words.count(w) for w in words}
print(word_count)

recursive_words=[k for k,v in word_count.items() if v>1 ]
print(recursive_words)

non_recursive_words=[k for k,v in word_count.items() if v==1]
print(non_recursive_words)

