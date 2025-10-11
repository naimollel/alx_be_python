from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    print("\n--- Library Collection ---")
    my_library.list_books()

    # Demonstrate __str__ and __repr__ using one of the books
    print("\n--- Book Representations ---")
    print(classic_book)          # Expected to use __str__
    print(repr(classic_book))    # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    print("\n--- Deleting a book instance ---")
    del classic_book


if __name__ == "__main__":
    main()
