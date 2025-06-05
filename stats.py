def get_word_count(text):
    return len(text.split())


def get_letter_counts(text):
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts
