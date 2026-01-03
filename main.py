import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def print_report(filepath, num_words, chars_sorted_list):
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============\n")


def main():
    if len(sys.argv) != 2:
        print("\nERROR: Filepath to a book or text-file required.")
        print("Usage: python3 main.py <path_to_book>\n")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(filepath, num_words, chars_sorted_list)


main()