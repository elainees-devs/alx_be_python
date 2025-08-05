class Book:
    def __init__(self, title: str, author: str, year: int = 0):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __del__(self):
        print(f"Deleting book: {getattr(self, 'title', 'Unknown')}")


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: str, year: int = 0):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', '{self.file_size}')"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int, year: int = 0):
        super().__init__(title, author, year)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"
