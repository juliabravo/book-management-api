from fastapi import FastAPI
from library_system import Library, Book

app = FastAPI()
my_library = Library()
# my_library.add_book(Book('Hocus Pocus', 'Kurt Vonnegut', 324, False))
# my_library.add_book(Book('', 'No One', -10, False))

@app.get("/")
def root():
    return {"message": "Library Management API Online"}

@app.get("/books")
def show_books():
    book_list =[]
    for book in my_library.books:
        book_list.append(book.to_dict())
    
    return book_list
    
@app.get("/stats")
def show_library_stats():
    library_stats = {
        "total_books": len(my_library.books),
        "total_pages": my_library.get_total_pages(),
        "unread_count": my_library.get_unread_count()
    }
    return library_stats