text=["apple","iphone","oranges","potato"]

vowels_words=[w for w in text if w[0] in ['a','e','i','o','u']]
print(vowels_words)



consonant_words=[w for w in text if w[0] not in("aeiou")]
print(consonant_words)


#longest_word

long=max([len(w) for w in text])
longest_word=[w for w in text if len(w)==long]
print(longest_word)