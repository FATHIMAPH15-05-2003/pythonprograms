user=["rahul","rohil","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohil","kohli","rishab"]
follow_suggestion=["sanju","pandya","siraj"]

rahul_follow_suggestion=set(user).difference(set(rahul_followers))
print(rahul_follow_suggestion)





rahul_followers=["rohil","kohli","rishab"]
sanju_followers=["sanju","rohot","kohli"]
mutual_frinds=set(rahul_followers).intersection(set(sanju_followers))
print(mutual_frinds)