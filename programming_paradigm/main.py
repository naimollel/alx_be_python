import sys
from robust_division_calculator import safe_divide
from library_management import Book, Library


def run_division():
    """
    Command-line interface for performing safe division.
    Usage:
        python main.py <numerator> <denominator>
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division using safe_divide function
    result = safe_divide(numerator, denominator)
    print(f"\nSafe Division Result: {result}")


def run_library_demo():
    """Demonstrates the Library and Book classes."""
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("\nAvailable books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


def main():
    # Run the safe division first
    run_division()

    # Then run the library demo
    run_library_demo()


if __name__ == "__main__":
    main()
