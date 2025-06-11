

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

def main():
    filename = ['books/3.txt','books/4.txt','books/5.txt']
    for f in filename:
        book_stats(f)

main()
