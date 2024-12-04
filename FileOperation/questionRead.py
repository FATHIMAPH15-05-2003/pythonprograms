f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\question.txt")
words=[]
for line in f:
    line=(line.rstrip("\n"))
    all_words=line.split(" ")

    for w in all_words:
        words.append(w)
# print(words)    

words_count={w:words.count(w) for w in words}
# print(words_count)

nested_word_count=[[v,k] for k,v in words_count.items()]
print(sorted(nested_word_count,reverse=True))
    

