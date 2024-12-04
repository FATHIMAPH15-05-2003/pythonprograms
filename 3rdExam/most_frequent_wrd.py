text="this is a simple python program that print most recursive word"
words=text.split(" ")

def get_count(w):
    return words.count(w)

frequent_words=max(words,key=get_count)
print(frequent_words)