def get_word_count(text):
    return len(text.split())


def get_letter_counts(text):
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts


def sort_letter_counts(letter_counts: dict[str, int]) -> list[dict[str, str|int]]:
    char_list = []
    for char in letter_counts:
        char_list.append({"char": char, "num": letter_counts[char]})

    char_list.sort(reverse=True, key=lambda d: d["num"])

    return char_list
