class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __del__(self):
        print(f"Deleting book: {self.title}")


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: float):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()}, file size: {self.file_size}MB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.year}, {self.file_size})"


class PrintBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, page_count: int = 0):
        super().__init__(title, author, year)
        self.pages = pages
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()}, {self.pages} pages"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.pages})"

    def __del__(self):
        print(f"Deleting book: {self.title}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Library Collection:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def find_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
