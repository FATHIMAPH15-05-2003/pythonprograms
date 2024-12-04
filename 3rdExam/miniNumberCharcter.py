text="this is a simple question return word with maximum number of character"

words=text.split(" ")

longest_word=max(words,key=len)
print(longest_word)