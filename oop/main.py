from book_class import Book
from library_system import EBook, PrintBook, Library

def main():
    # Create an instance of Book
    book1 = Book("1984", "George Orwell", 1949)
    # Create instance of the Library
    my_library = Library()
    
    # Print the book using __str__
    print(book1)
    
    # Print the book using __repr__
    print(repr(book1))
    
    # Delete the book instance
    del book1

        # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()