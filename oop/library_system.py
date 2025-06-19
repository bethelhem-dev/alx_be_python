# library_system.py

class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size  # size in KB

    def __str__(self) -> str:
        return (
            f"EBook: {self.title} by {self.author}, "
            f"File Size: {self.file_size}KB"
        )


class PrintBook(Book):
    """Derived class representing a printed (paper) book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return (
            f"PrintBook: {self.title} by {self.author}, "
            f"Page Count: {self.page_count}"
        )


class Library:
    """Class that manages a collection of books (composition)."""
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError(
                "add_book expects an instance of Book or its subclasses"
            )
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(book)
