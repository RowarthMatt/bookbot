import sys

from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list_of_characters

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def print_report(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted = sorted_list_of_characters(num_characters)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 2:
        print_report(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()