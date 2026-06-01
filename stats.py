from typing import TypedDict


class CharacterCount(TypedDict):
    char: str
    num: int


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d: CharacterCount) -> int:
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[CharacterCount]:
    sorted_list: list[CharacterCount] = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
