def count_words(content):
    split_content = content.split()
    num_words = len(split_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def count_chars(content):
    content_lowercase = content.lower()
    counter = {}

    for char in content_lowercase:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    print("--------- Character Count -------")
    print_sorted_list(counter)

def print_sorted_list(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    for dict in sorted_dict:
        if dict[0].isalpha():
            print(f"{dict[0]}: {dict[1]}")        