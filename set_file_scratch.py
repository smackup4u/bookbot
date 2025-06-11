

def read_file(path):
    text_string = ''
    with open(path) as f:
        text_string = f.read()
    return text_string

def get_unique_words(text_str):
    split_words = []
    split_words = text_str.split()
    return split_words


def main():
    filename = 'frankenstein.txt'
    textfile_plain = ''
    textfile_plain = read_file(filename)
    word_list = []
    word_list = get_unique_words(textfile_plain)
    print(word_list[89])

main()
