def word_count(sentence):
    words=sentence.split()
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency
sentence="my name is fathima"
print(word_count(sentence))