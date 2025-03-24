path_to_book = "/home/silentspecter/Workspace/github.com/simonskij/bookbot/books/frankenstein.txt"

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text(path_to_book))

main()
