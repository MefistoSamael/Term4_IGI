from GlobalConstants import FILES_PATH
import re

# Abbreviations

BIG_LETTER_ABBREVIATIONS = (r"\bMr\.", r"\bMrs\.", r"Dr\.", r"St\.", r"Blvd\.", r"Ave\.", r"Sq\.",
                            r"Rd\.", r"Bldg\.", r"B\.Sc\.", r"M\.A\.", r"Ph\.D\.", r"M\.D\.", r"LT\.",
                            r"Mx\.", r"Esq\.", r"Dr\.", r"KC\.", r"Fr\.", r"Pr\.", r"Br\.", r"Sr\.", r"Ph\.D\.")

OTHER_ABBREVIATIONS = (r"etc\.", r"Re\.", r"p\.", r"exp\.", r"err\.", r"et\.al\.", r"ex\.",
                       r"e\.g\.", r"fin\.", r"i\.e\.", r"vs\.", r"N\.B\.", r"P\.S\.", r"P\.P\.S\.",
                       r"P\.S\.S\.", r"ft\.", r"oz\.", r"pt\.", r"in\.", r"sec\.", r"\bg\.",
                       r"cm\.", r"qt\.", r"p\.m\.")

# Files

TEST_FILE_PATH = FILES_PATH + "test_file.txt"
TESTS = FILES_PATH + "Tests/"

# REGEX

ALL_NUMBERS = r"\b\d+e[+-]\d+|\b\d+[.,]?\d+|\b\d+"
EXTRA_CHARACTERS = r"[!.?\",']"
FILE_NAME = r"\w+\.\w+"
ELLIPSIS = r"\.\.\."
BEGINNING_DIRECT_SPEACH_SPECIAL = r'\"[\w\d\s,\'!?.]*[?!]\"\s[a-z]'
END_DIRECT_SPEACH = r', \"[\w\d\s,\'!?.]*[?!.]\"'
BEGINNING_DIRECT_SPEACH = r'\"[\w\d\s,\'!?.]*,\"'
SEPARATE_SENTENCE = r'\"[\w\d\s,\'!?.]*[?!.]\"'
INITIALS = r"[A-Z]\. [A-Z]\. [A-Z]"
BEGINNING_SENTENCE = r"\s[A-Z]"
END_OF_ALL_SENTENCE = r"\w[.!?]"
END_OF_SENTENCE = r"\w[!?]"

# Commands

DISAGREE = 'n'
AGREE = 'y'

