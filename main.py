from stats import get_word_count, get_letter_counts, sort_letter_counts
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    num_words = get_word_count(file_contents)
    letter_counts = get_letter_counts(file_contents)
    letter_counts_sorted = sort_letter_counts(letter_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter_count in letter_counts_sorted:
        if not letter_count['char'].isalpha():
            continue
        print(f"{letter_count['char']}: {letter_count['num']}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


main()
