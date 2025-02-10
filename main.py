from typing import Dict
import string

def main():
    path_book = "books/frankenstein.txt"
    with open(path_book) as book:
            book_content = book.read()

    # print(book_content)
    # print(count_words(book_content))
    # print(count_characters(book_content))
    print (report(text=book_content))

def count_words(text: str) -> int:
    """Function who count the number of words from a text"""
    words = text.split()
    return len(words)

def count_characters(text: str) -> Dict:
    char = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in char:
            char[lower_letter] += 1
        else:
            char[lower_letter] = 1

    return char

def report(text: str) -> str:

    rep = "--- Begin report of books/frankenstein.txt ---"
    rep += "\n"

    # adding words to the report
    total_words = count_words(text)
    rep += f"{total_words} words found in the document"
    rep += "\n\n"

    # adding each letters to the report
    char = count_characters(text)

    alphabet = string.ascii_lowercase

    for key_char in char:
        if key_char in alphabet:
            rep += f"The '{key_char}' character was found {char[key_char]} times"
            rep += "\n"

    return rep

if __name__ == "__main__":
    main()

