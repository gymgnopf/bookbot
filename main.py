from stats import count_words, count_chars

def main():
    content = get_book_text('books/frankenstein.txt')
    num_words = count_words(content)
    print(f"{num_words} words found in the document")
    print(count_chars(content))

def get_book_text(path):
    with open(path) as f:
        return f.read()
main()