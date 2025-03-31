from stats import get_book_words, char_count, char_count_list
import sys


def get_book_text(filepath):
    text_file = ""
    with open(filepath) as f:
        text_file = f.read()
    return text_file
def sort_on(dict):
    return dict["count"] 
       
def main():
    print_text = ""
    word_count = 0
    char_c = {}
    char_c2 = {}
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print_text = get_book_text("books/frankenstein.txt")
    print_text = get_book_text(sys.argv[1])
    word_count = get_book_words(print_text)
    char_c = char_count(print_text)
    #print(f"{word_count} words found in the document")
    char_c2 = char_count_list(char_c)
    char_c2.sort(reverse=True, key=lambda char_c2: char_c2["count"])
    print("===BOOKBOT===")
    print("Analysing book")
    print("-----Word count----")
    print(f"Found {word_count} total words")
    print("----character count----")
    for c in char_c2:
        print(f"{c['char']}: {c['count']}")
    #print(char_c2)
    #print(sys.argv[0])

main()
