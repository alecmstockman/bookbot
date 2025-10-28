def get_books_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(file_path):
    text = get_books_text(file_path)
    parts = text.split()
    return len(parts)

# num_words = word_count()

def character_count(file_path):
    new_dict = {}
    char_list = []
    text = get_books_text(file_path).lower()
    for char in text:
        if char not in char_list:
            char_list.append(char)
    for char in char_list:
        count = text.count(char)
        new_dict[char] = count
    return new_dict


def sorted_dict(file_path):
    char_count = character_count(file_path)
    new_list = []
    for char in char_count:
        dict = {}
        dict["char"] = char
        dict["num"] = char_count[char]
        new_list.append(dict)
    sorted_list = sorted(new_list, key=lambda x: x['num'], reverse=True)
    return sorted_list



