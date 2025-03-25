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