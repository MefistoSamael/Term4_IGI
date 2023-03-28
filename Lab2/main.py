from utilities import get_sentences_amount, get_not_declarative_sentences_amount, get_average_sentence_length,\
                      get_average_word_length, n_grams
from constants import PATH, K, N
import re

if __name__ == "__main__":
    with open(PATH + 'test_file.txt') as f:
        text = f.read()

    print(text)

    count = get_sentences_amount(text)
    print(f"{count} - amount of sentences in the text")

    print(f"{get_not_declarative_sentences_amount(text)} - amount of non-declarative sentences in the text ")

    print(f"{get_average_sentence_length(text)} - average length of the sentence in characters. Counts only words")

    print(f"{get_average_word_length(text)} - average length of the word in the text in characters")

    print(f"top-{K} repeated {N}-grams in the text:")
    for gram in n_grams(text, N)[:K]:
        print(gram)
