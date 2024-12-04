# example

def add_number(num1,num2):
    return num1+num2
print(add_number(3,2))

#converted to lambda
add_number=lambda num1,num2:num1+num2
print(add_number(5,2))


#max two

def max_two(str1,str2):
    return str1 if len(str1)>len(str2) else str2


max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("apple","oranges"))

#smart_sub

def smart_sub(num1,num2):
    return num1-num2 if num1>num2 else num2-num1
print(smart_sub(5,3))

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(5,3))



#string length
words=["apple","hai","hello","morning"]
def get_length(words):
    return len(words)
print(max(words,key=get_length))


lambda words:len(words)
print(max(words,key=get_length))

# maximum words
text="this is a simple programming language questions"
words=text.split(" ")
print(max(words))
def get_length(words):
    return len(words)
print(max(words,key=get_length))






#sort
word=["hello","hai","morning","text","apple"]
def get_length(words):
    return len(word)
srt_words=sorted(word,key=get_length)
print(srt_words)


#most recursive words
text="this is a simple programming language this is simple"
words=text.split(' ')
def get_count(w):
    return words.count(w)
print(max(words,key=get_count))

#most frequent count
text="AABCBBDC"
def get_count(char):
    return text.count(char)
print(max(text,key=get_count))

