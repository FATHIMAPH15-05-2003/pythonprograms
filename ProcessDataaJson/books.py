from json import load
f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\books.json")

data=load(f)
# print(data)


# all_titles=[book.get("title")for book in data]
# print(all_titles)


# for book in data:
#     print(book)


# pages_filter=[book.get("title") for book in data if book.get("pages")< 250]
# print(pages_filter)



# all_genre=[book.get("genre") for book in data]
# print(all_genre)


# costly_book=[max(data,key=lambda d:d.get("price"))]
# print(costly_book)

#author with more than one book

all_author=[book.get("author") for book in data]

author_count={auth:all_author.count("auth") for auth in all_author}

print([k for k,v in author_count.items() if v>1])

