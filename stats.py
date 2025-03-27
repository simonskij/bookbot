def count_words(text):
    words = text.split()
    return len(words)


def get_character_dict(text):
    character_dict = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in character_dict:
                character_dict[letter] += 1
            else:
                character_dict[letter] = 1
    return character_dict   

def get_split_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        new_item = {"char": char, "count": count} 
        char_list.append(new_item)
    return char_list


def sort_count(char_dict):
    return char_dict["count"]
