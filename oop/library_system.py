class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is being destroyed."""
        print(f"Deleting book: {self.title}")


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: float):
        """Constructor: Initializes an Ebook instance with title, author, year, and file size."""
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """Returns a readable string representation of the ebook."""
        return f"{self.title} by {self.author}, published in {self.year}, file size: {self.file_size}MB"

    def __repr__(self):
        """Returns a formal string representation that can recreate the Ebook object."""
        return f"Ebook('{self.title}', '{self.author}', {self.year}, {self.file_size})"


class PrintBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int):
        """Constructor: Initializes a PrintBook instance with title, author, year, and number of pages."""
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        """Returns a readable string representation of the print book."""
        return f"{self.title} by {self.author}, published in {self.year}, {self.pages} pages"

    def __repr__(self):
        """Returns a formal string representation that can recreate the PrintBook object."""
        return f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.pages})"
        print(f"Deleting book: {self.title}")

class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("Library Collection:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")