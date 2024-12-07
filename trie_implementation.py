class TrieNode:
    def __init__(self):
        self.children = {}
        self.books = [] 


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, book):
        node = self.root
        for char in key.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.books.append(book)

    def search_by_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return [] 
            node = node.children[char]
        return node.books


author_trie = Trie()
title_trie = Trie()


def add_book(author, title, year, genre):
    book = {"author": author, "title": title, "year": year, "genre": genre}
    # Insert into the author trie
    author_trie.insert(author, book)
    # Insert into the title trie
    title_trie.insert(title, book)


def search_books_by_author_prefix(prefix):
    return author_trie.search_by_prefix(prefix)


def search_books_by_title_prefix(prefix):
    return title_trie.search_by_prefix(prefix)


# Adding some books
add_book("J.K. Rowling", "Harry Potter", 1997, "Fantasy")
add_book("George Orwell", "1984", 1949, "Dystopian")
add_book("J.K. Rowling", "Fantastic Beasts", 2001, "Fantasy")
add_book("George R.R. Martin", "A Game of Thrones", 1996, "Fantasy")

# Searching by author prefix
print("Books by authors starting with 'J.K.':")
for book in search_books_by_author_prefix("J.K."):
    print(book)

# Searching by title prefix
print("\nBooks with titles starting with 'Harry':")
for book in search_books_by_title_prefix("Harry"):
    print(book)

# Searching by partial author prefix
print("\nBooks by authors starting with 'George':")
for book in search_books_by_author_prefix("George"):
    print(book)

# Searching by a non-existent prefix
print("\nBooks with titles starting with 'Unknown':")
print(search_books_by_title_prefix("Unknown"))
