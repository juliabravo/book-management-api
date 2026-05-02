from fastapi import FastAPI, HTTPException
from library_system import Library, Book
from pydantic import BaseModel
from datetime import date

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

class BookSchema(BaseModel):
    title: str
    author: str
    pages: int
    is_read: bool

@app.post("/books")
def create_book(book_data: BookSchema):
    new_book = Book(book_data.title, book_data.author, book_data.pages, book_data.is_read)
    my_library.add_book(new_book)
    my_library.save_to_file()
    return new_book.to_dict()

class LogSchema(BaseModel):
    pages: int

@app.post("/books/{title}/log")
def update_log(title: str, log_data: LogSchema):
    book_found = False
    for book in my_library.books:
        if book.title.lower() == title.lower():
            book.log_progress(log_data.pages)
            book_found = True
            break
    if not book_found:
        raise HTTPException(status_code=404, detail="Book Not Found")
    my_library.save_to_file()
    return {"status": "success", "message": f"Logged {log_data.pages} pages for {title}"}

@app.get("/daily-total")
def get_daily_total():
    today = str(date.today())
    total_pages = 0

    for book in my_library.books:
        for log in book.progress_log:
            if log["date"] == today:
                total_pages += log["pages"]
    
    return {"date": today, "total_pages": total_pages}