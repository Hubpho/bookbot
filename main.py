def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


main()
