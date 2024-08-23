def get_book(book_path):
    with open(book_path) as f:
        book_words = f.read()
        words_lowered = book_words.lower()
        
    return words_lowered #return all the words seperated into a list

def count_characters(words_lowered):
    character_count = {}  #Create an empty dict to store values
    total_word_count = 0
    for word in words_lowered:
       
       if word.isalpha():
            total_word_count +=1

       for char in word:
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1
    
    return character_count, total_word_count #returns the total character count for each letter used in the text

def get_total_char_count(char_count):
    total_count = 0
    for key in char_count:
        print(char_count[key])
        total_count += char_count[key]
    return total_count

def sort_on(dict):
    pass

def print_report(total_word_count, book_path,char_count):
   print(f"--- Begin report of {book_path} ---\n")
   print(f"{total_word_count} words found in the document")
   print()
   print()
   for key in char_count:
       if key.isalpha():
           print(f"The '{key}' character was found {char_count[key]} times")
   print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    words_lowered = get_book(book_path)
    char_count, total_word_count = count_characters(words_lowered)
    print_report(total_word_count, book_path, char_count)

main()