import re
from constants import *


def clear_text(text):
    substr = text

    for abbr in BIG_LETTER_ABBREVIATIONS:
        substr = re.sub(abbr, " ", substr)

    # File name
    substr = re.sub(r"\w+\.\w+", " ", substr)

    # Ellipsis
    substr = re.sub(r"\.\s\.\s\.", ".", substr)

    # Direct speech - the end of a sentence
    substr = re.sub(r', \"[\w\d\s,\'!?.]*[?!.]\"', ".", substr)

    # Direct speech - the beginning of a sentence
    substr = re.sub(r'\"[\w\d\s,\'!?.]*,\"', 'A,', substr)

    # Direct speech - a separate sentence
    substr = re.sub(r'\"[\w\d\s,\'!?.]*[?!.]\"', 'A.', substr)

    # Initials
    substr = re.sub(r"[A-Z]\. [A-Z]\. [A-Z]", " ", substr)

    for abbr in OTHER_ABBREVIATIONS:
        # Sentence after an abbreviation
        substr = re.sub(abbr + r"\s[A-Z]", ". ", substr)
        substr = re.sub(abbr, " ", substr)

    return substr


def sentences_amount(text):
    return len(re.findall(r"[.!?]", clear_text(text)))


def not_declarative_sentences(text):
    return len(re.findall(r"[!?]", clear_text(text)))