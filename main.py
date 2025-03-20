from stats import count_words, count_chars, sort_chars
import sys

def main():

    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = get_book_text(file_path)
    num_words = count_words(content)
    num_chars = count_chars(content)
    num_chars = sort_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for num in num_chars:
        print(f"{num['char']}: {num['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
main()