from stats import get_word_count, get_char_report, get_sorted_res

import sys

def get_book_text(filepath):

    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():

    # filepath = "books/frankenstein.txt"
    # print(get_book_text("books/frankenstein.txt"))

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    file_content = get_book_text(filepath)

    res = get_char_report(file_content)

    # print(f"{get_word_count(file_content)} words found in the document")

    # for i in res:
    #     print(f"'{i}': {res[i]}")

    res_list = get_sorted_res(res)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")

    print(f"Found {get_word_count(file_content)} total words")

    print("--------- Character Count -------")

    for dict in res_list:
        print(f"{dict["char"]}: {dict["num"]}")


main()
