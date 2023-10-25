class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author_name(self):
        return self.author.name

    def __str__(self):
        return f" the title {self.title}, and the auther {self.author.name}"

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)


# Create instances of authors and books
author1 = Author("J.K. Rowling")
author2 = Author("George Orwell")

book1 = Book("Harry Potter and the Sorcerer's Stone", author1)
book2 = Book("the year 1984", author2)
book3 = Book("I donot know", author1)

# Associate books with authors
author1.add_book(book1)
author1.add_book(book3)
author2.add_book(book2)

# Demonstrate association
for author in [author1, author2]:
    print(f"Author: {author.name}")
    print("Books written by the author:")
    for book in author.books:
        print(f"- {book.title}")
    print()

# Get the author of a book
print(f"The author of 'the year 1984' is {book2.get_author_name()}")

print(book1)