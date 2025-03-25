path_to_book = "/home/silentspecter/Workspace/github.com/simonskij/bookbot/books/frankenstein.txt"

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import get_character_dict

def main():
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    character_dict = get_character_dict(book_text)
    print(f"{word_count} words found in the document")
    print(character_dict)
main()
