class Book:

    def __init__(self, title, author, pages, is_read):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def describe(self):
        if self.is_read:
            status = "Read"
        else:
            status = "Unread"

        return (f"{self.title} by {self.author} ({self.pages} pages- Status: {status})")

    def read_book(self):
        self.is_read = not self.is_read

    def update_page_count(self, pages):
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_inventory(self):
        return [book.describe() for book in self.books]

    def get_unread_count(self):
        count = 0
        for book in self.books:
            if not book.isread:
                count += 1
        return count
    
    def get_titles_only(self):
        return [book.title for book in self.books]
    
    def find_by_author(self, author_name):
        books_by_author = []
        for book in self.books:
            if book.author.lower() == author_name.lower():
                books_by_author.append(book)
            else: 
                continue
        return books_by_author

        

# create books
book1 = Book('Crime and Punishment', 'Fyodor Dostoevsky', 557, True)
book2 = Book('Hocus Pocus', 'Kurt Vonnegut', 324, False)

# create library and add books
my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)

print("--- Initial Inventory ---")
my_library.list_inventory()

# change status
book2.read_book()

print("\n---Updated Inventory ---")
my_library.list_inventory()

print(my_library.list_inventory())
print(my_library.get_titles_only())

my_library.find_by_author(input("author name: "))