from library_system import Book, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle
from class_static_methods_demo import Calculator
import math


# --- 1. Library System Demo ---
def library_demo():
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books
    print("\n--- Library Collection ---")
    my_library.list_books()

    # Demonstrate __str__ and __repr__
    print("\n--- Book Representations ---")
    print(classic_book)
    print(repr(classic_book))

    # Trigger __del__
    print("\n--- Deleting a book instance ---")
    del classic_book


# --- 2. Book Class Demo ---
def book_demo():
    my_book = Book("1984", "George Orwell", 1949)

    print("\n--- Book Class Demo ---")
    print(my_book)
    print(repr(my_book))

    del my_book


# --- 3. Polymorphism Demo ---
def polymorphism_demo():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    print("\n--- Polymorphism Demo ---")
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")


# --- 4. Class & Static Methods Demo ---
def calculator_demo():
    print("\n--- Class & Static Methods Demo ---")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


# --- Main Controller ---
def main():
    print("===== Running Library System Demo =====")
    library_demo()

    print("\n===== Running Book Class Demo =====")
    book_demo()

    print("\n===== Running Polymorphism Demo =====")
    polymorphism_demo()

    print("\n===== Running Calculator Demo =====")
    calculator_demo()


if __name__ == "__main__":
    main()
