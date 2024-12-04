order=["tea","coffee","tea","coffee","porotta"]
order_summery={}
for items in order:
    if items in order_summery:
        order_summery[items]+=1
    else:
        order_summery[items]=1
print(order_summery)       



text="ABCBBCA"
char_count={}
for ch in text:
    if ch in char_count:
        char_count[ch]+=1
    else:
        char_count[ch]=1
print(char_count)        
