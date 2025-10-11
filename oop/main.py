from library_system import Book, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle
import math

def library_demo():
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

    # Demonstrate __str__ and __repr__
    print("\n--- Book Representations ---")
    print(classic_book)          # Uses __str__
    print(repr(classic_book))    # Uses __repr__

    # Trigger __del__ by deleting a book instance
    print("\n--- Deleting a book instance ---")
    del classic_book


def book_demo():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrate __str__ and __repr__
    print("\n--- Book Class Demo ---")
    print(my_book)
    print(repr(my_book))

    # Deleting to trigger __del__
    del my_book


def polymorphism_demo():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    print("\n--- Polymorphism Demo ---")
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")


def main():
    print("===== Running Library System Demo =====")
    library_demo()

    print("\n===== Running Book Class Demo =====")
    book_demo()

    print("\n===== Running Polymorphism Demo =====")
    polymorphism_demo()


if __name__ == "__main__":
    main()
