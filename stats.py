def main(path_to_file):
    get_num_words(path_to_file)
    get_num_chars(path_to_file)
    list_sort(path_to_file)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(path_to_file):
    text = get_book_text(path_to_file)
    split_text = text.split()
    num_words = len(split_text)
    return num_words

def get_num_chars(path_to_file):
    text = get_book_text(path_to_file)
    num_chars = {}
    for character in text:
        char = character.lower()
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def list_sort(path_to_file):
    unsorted = get_num_chars(path_to_file)
    num_words = get_num_words(path_to_file)
    sorted_list = []
    for char in unsorted:
        if char.isalpha():
            sorted_list.append({"char": char, "num": unsorted[char]})

    def sort_on(list_item):
        return list_item["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for list_item in sorted_list:
        print(f"{list_item['char']}: {list_item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
