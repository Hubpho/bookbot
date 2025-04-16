import sys
from stats import get_num_words, get_num_chars, list_sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    get_num_words(path_to_file)
    get_num_chars(path_to_file)
    list_sort(path_to_file)

main()
