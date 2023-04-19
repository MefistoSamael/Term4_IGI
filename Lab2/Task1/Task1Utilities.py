import re
from Task1.Task1Constants import BIG_LETTER_ABBREVIATIONS, OTHER_ABBREVIATIONS, EXTRA_CHARACTERS, ALL_NUMBERS, \
    FILE_NAME, ELLIPSIS, BEGINNING_DIRECT_SPEACH_SPECIAL, END_DIRECT_SPEACH, BEGINNING_DIRECT_SPEACH, \
    SEPARATE_SENTENCE, INITIALS, BEGINNING_SENTENCE, END_OF_ALL_SENTENCE, END_OF_SENTENCE


def simplify_text(text):
    substr = text

    for abbr in BIG_LETTER_ABBREVIATIONS:
        substr = re.sub(abbr, " ", substr)

    # File name
    substr = re.sub(FILE_NAME, " ", substr)

    # Ellipsis
    substr = re.sub(ELLIPSIS, ".", substr)

    # checks the beginning of a sentence with direct speech, but with ! or ?
    substr = re.sub(BEGINNING_DIRECT_SPEACH_SPECIAL, "A,", substr)

    # checks the end of a sentence with direct speech
    substr = re.sub(END_DIRECT_SPEACH, ".", substr)

    # checks the beginning of a sentence with direct speech
    substr = re.sub(BEGINNING_DIRECT_SPEACH, 'A,', substr)

    # Direct speech - a separate sentence
    substr = re.sub(SEPARATE_SENTENCE, 'A.', substr)

    # Initials
    substr = re.sub(INITIALS, " ", substr)

    for abbr in OTHER_ABBREVIATIONS:
        # Sentence after an abbreviation
        substr = re.sub(abbr + BEGINNING_SENTENCE, ". ", substr)
        substr = re.sub(abbr, " ", substr)

    return substr


def get_sentences_amount(text):
    return len(re.findall(END_OF_ALL_SENTENCE, simplify_text(text)))


def get_not_declarative_sentences_amount(text):
    return len(re.findall(END_OF_SENTENCE, simplify_text(text)))


def get_average_sentence_length(text):
    words_length = 0
    sentences_amount = get_sentences_amount(text)

    if not sentences_amount:
        return 0

    for word in split_into_words(text):
        words_length += len(word)

    return round(words_length / sentences_amount)


def split_into_words(text):
    # Removes all numbers
    str = re.sub(ALL_NUMBERS, " ", text)
    # Removes extra character
    str = re.sub(EXTRA_CHARACTERS, " ", str)
    str = re.sub(":", " ",str)
    return str.split()


def get_average_word_length(text):
    all_words = split_into_words(text)

    if not len(all_words):
        return 0

    words_length = 0

    for word in all_words:
        words_length += len(word)

    return round(words_length / len(all_words))


def n_grams(text, n, k):
    # Change input data is very bad habit
    no_arg_text = text.lower()
    words = split_into_words(no_arg_text)
    ngrams = dict()

    for i in range(len(words) - (n - 1)):
        # Gets ngram
        ngram = " ".join(words[i: i + n])

        # If ngram were founded before
        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1

    return sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:k]
