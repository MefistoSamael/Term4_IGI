from utilities import sentences_amount, not_declarative_sentences
from constants import PATH
import re

if __name__ == "__main__":
    print(PATH, "     ", PATH + 'test_file.txt')
    with open(PATH + 'test_file.txt') as f:
        text = f.read()
    print(text)

    count = sentences_amount(text)
    print(f"amount of sentences in the tex: {count}")

    print(f"amount of non-declarative sentences in the tex: {not_declarative_sentences(text)}")