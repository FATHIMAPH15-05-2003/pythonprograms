read_path="C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\words.txt"
write_path="C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\palindromes.txt"

f_read=open(read_path)
f_write=open(write_path,"w")



for line in f_read:
    words=line.rstrip("\n")
    reversed_word=words[::-1]
    if words==reversed_word:
        f_write.write(words+"\n")

f_read.close()
f_write.close()       