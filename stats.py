def get_book_words(book_string):
    split_temp = ""
    split_temp = book_string.split()
    return len(split_temp)

def char_count(book_string):
    lower_str = ""
    lower_str = book_string.lower() # just lower characters the whole text
    char_c = {} # initialize empty directory
    for char in lower_str:
        if char in char_c:
            char_c[char] += 1 # increment count
        else:
            char_c[char] = 1
    return char_c

def char_count_list(c_dict):
    list_of_chars = []
    for char, count in c_dict.items():
        if char.isalpha():
            list_of_chars.append({'char': char, 'count': count})
    return list_of_chars