import sys
from stats import get_num_words
from stats import get_num_letters
from stats import sort_dictionary


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    #filepath = "books/frankenstein.txt"
    try:    
        filepath = sys.argv[1]
        book = get_book_text(filepath)
        sorted_dict = sort_dictionary(book)
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print(f"----------- Word Count ----------")
        print(f"Found {get_num_words(book)} total words")
        print(f"--------- Character Count -------")
        for item in sorted_dict:        
            if item.isalpha():
                print(f"{item}: {sorted_dict[item]}")
        print(f"============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()