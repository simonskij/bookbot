path_to_book = "/home/silentspecter/Workspace/github.com/simonskij/bookbot/books/frankenstein.txt"

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import get_character_dict
from stats import get_sorted_dict

def main():
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    character_dict = get_character_dict(book_text)
    sorted_dict = get_sorted_dict(character_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sorted_dict)
    print("============= END ===============")
main()
