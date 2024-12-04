text1="abc"
text2="pqr"
def merged_string(text1,text2):
    merged_string=[]

    len1, len2 = len(text1), len(text2)
    for i in range(max(len1, len2)):
        if i < len1:
            merged_string.append(text1[i])
        if i < len2:
            merged_string.append(text2[i])
    return ''.join(merged_string)
# text1="abc"
# text2="pqr"

result=(merged_string(text1,text2))
print(result)
  










# # 
# # 
# #         
# def merge_strings(word1, word2):
#     merged_string = []
#     len1, len2 = len(word1), len(word2)
#     for i in range(max(len1, len2)):
#         if i < len1:
#             merged_string.append(word1[i])
#         if i < len2:
#             merged_string.append(word2[i])
#     return ''.join(merged_string)
# word1 = "abc"
# word2 = "pqr"
# result = merge_strings(word1, word2)
# print(result) 