# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Command-line interface for performing safe division.
    Usage:
        python main.py <numerator> <denominator>
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division using safe_divide function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
