path_to_book = "/home/silentspecter/Workspace/github.com/simonskij/bookbot/books/frankenstein.txt"

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import get_character_dict
from stats import get_split_dict
from stats import sort_count

def main():
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    character_dict = get_character_dict(book_text)
    split_dict = get_split_dict(character_dict)


    split_dict.sort(reverse=True, key=sort_count)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in split_dict:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()
