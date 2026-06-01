from stats import get_chars_dict, get_num_words


def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print(chars_dict)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


main()
