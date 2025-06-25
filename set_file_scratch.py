import os
import datetime


def read_file(path):
    text_string = ''
    with open(path) as f:
        text_string = f.read()
    return text_string

def get_unique_words(text_str):
    split_words = []
    split_words = text_str.split()
    return split_words

def book_stats(filename):
    print(filename)
    print('++++++++++++++++++++++++++++')
    textfile_plain = ''
    textfile_plain = read_file(filename)
    word_list = []
    word_list = get_unique_words(textfile_plain.lower())
    # print(word_list[89])
    uniques = set(word_list)
    print(f'Der Text hat insgesamt {len(word_list)} Woerter und {len(uniques)} unterschiedliche Woerter')

def get_books_guten(first_b, last_b):
    for bo in range(first_b, last_b + 1):
        command_curl = 'curl --output books/'  + str(bo) + '.txt "https://www.gutenberg.org/cache/epub/' + str(bo) + '/pg' + str(bo) + '.txt"'
        os.system(command_curl)

def main():
    list_files = os.listdir('./books')
    list_files.sort()
    print(list_files)
    filename = ['books/81.txt','books/84.txt','books/85.txt']
    for f in list_files:
        f_dir = 'books/' + f
        book_stats(f_dir)
    time = datetime.datetime.now()
    print(time)
    commandline = 'ls -l'
    #os.system(commandline)
    list_files = os.listdir('./books')
    list_files.sort()
    print(list_files)
    book_number = 89
    #command_curl = 'curl --output books/89.txt "https://www.gutenberg.org/cache/epub/89/pg89.txt"'
    first_book = 45
    last_book = 49
    get_books_guten(first_book, last_book)
main()
