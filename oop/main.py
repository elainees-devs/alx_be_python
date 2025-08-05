from book_class import Book
from library_system import EBook, PrintBook

def main():
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    digital_novel = EBook("Snow Crash", "Neal Stephenson", "500KB")
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    print(classic_book)
    print(digital_novel)
    print(paper_novel)

if __name__ == "__main__":
    main()
