class Book:
    def __init__(self, title: str, author: str, year: int = 0):
        """Constructor: Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Returns a readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a formal string representation that can recreate the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: Prints a message when the Book object is deleted."""
        print(f"Deleting {self.title}")
