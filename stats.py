def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    text = text.lower()
    character_count = {}
    for c in text:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1

    return character_count

def num_sort(e):
        return e["num"]

def sorted_list_of_characters(character_counts):
    chars = []
    for k in character_counts.keys():
        chars.append({"char": k, "num": character_counts[k]})
    sorted_chars = sorted(chars, key=num_sort, reverse=True)
    return sorted_chars

