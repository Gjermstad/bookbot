def get_num_words(content):
    split_content = content.split()
    return len(split_content)


def get_chars_dict(content):
    content_lowercase = content.lower()
    counter = {}

    for char in content_lowercase:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter


def chars_dict_to_sorted_list(counter):
    chars_list = []

    for char, num in counter.items():
        chars_list.append({"char": char, "num": num})

    chars_list.sort(key=lambda item: item["num"], reverse=True)
    return chars_list