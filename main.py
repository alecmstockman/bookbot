from stats import word_count, sorted_dict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    report(file_path)


def report(file_path):
    
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {file_path}\n"
        "----------- Word Count ----------\n"
        f"Found {word_count(file_path)} total words\n"
        "--------- Character Count -------"
    )
    for item in sorted_dict(file_path):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()