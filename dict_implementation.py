books_by_author = {}
books_by_title = {}

def add_book(author, title, year, genre):
    book = {"author": author, "title": title, "year": year, "genre": genre}
    
    if author not in books_by_author:
        books_by_author[author] = []
    books_by_author[author].append(book)
    
    books_by_title[title] = book

def search_by_author(author):
    return books_by_author.get(author, [])

def search_by_title(title):
    return books_by_title.get(title, None)

# Adding some books
add_book("J.K. Rowling", "Harry Potter", 1997, "Fantasy")
add_book("George Orwell", "1984", 1949, "Dystopian")
add_book("J.K. Rowling", "Fantastic Beasts", 2001, "Fantasy")

# Searching by author
print("Books by J.K. Rowling:")
for book in search_by_author("J.K. Rowling"):
    print(book)

# Searching by title
print("\nDetails of '1984':")
print(search_by_title("1984"))

# Searching for a non-existing author
print("\nBooks by Unknown Author:")
print(search_by_author("Unknown Author"))
