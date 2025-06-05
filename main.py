from stats import get_word_count, get_letter_counts


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(file_contents)
    print(f"{num_words} words found in the document")
    letter_counts = get_letter_counts(file_contents)
    print(letter_counts)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


main()
