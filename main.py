from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
        count_words(file_content)
        count_chars(file_content)

def main():
    filepath = "books/frankenstein.txt"
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    get_book_text(filepath)
    print("============= END ===============\n")

main()