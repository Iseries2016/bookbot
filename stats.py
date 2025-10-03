def get_num_words(booktext):
    book = booktext
    num_words = book.split()
    return len(num_words)

def get_num_letters(booktext):
    result = {}
    book = booktext
    num_strings = book.split()

    for word in num_strings:
        for char in word:
            character = char.lower()
            if character not in result:
                result[character] = 1
            else:
                result[character] += 1
    return result

def sort_dictionary(booktext):
    un_sorted_dict = get_num_letters(booktext)
    sorted_list = []
    sorted_items = sorted(un_sorted_dict.items(),key=lambda item:item[1],reverse=True)
    sorted_dict = dict(sorted_items)
    return(sorted_dict)