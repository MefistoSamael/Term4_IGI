import unittest
from Task1.Task1Utilities import get_sentences_amount, get_not_declarative_sentences_amount, \
    get_average_sentence_length, get_average_word_length, n_grams


class Task1Tests(unittest.TestCase):

    # First test block

    def test_amount_of_sentence_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        expected_amount_of_sentence = 6
        self.assertEqual(expected_amount_of_sentence, get_sentences_amount(test_input),
                         f'incorrect sentences amount {TEST}')

    def test_amount_of_non_declarative_sentence_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        expected_amount_of_non_declarative_sentence = 2

        self.assertEqual(expected_amount_of_non_declarative_sentence,
                         get_not_declarative_sentences_amount(test_input),
                         f'incorrect non declarative sentences amount {TEST}')

    def test_average_length_of_sentence_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        expected_average_length_of_sentence = 3

        self.assertEqual(expected_average_length_of_sentence, get_average_sentence_length(test_input),
                         f'incorrect average length of sentence {TEST}')

    def test_average_length_of_word_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        expected_average_length_of_word = 3

        self.assertEqual(expected_average_length_of_word, get_average_word_length(test_input),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_ngrams_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        K = 10
        N = 2

        expected_K_NGrams = [('abc abc', 5)]

        self.assertEqual(expected_K_NGrams, n_grams(test_input, N, K),
                         f'incorrect average length of the word {TEST}')

    # Second test block

    def test_amount_of_sentence_2(self):
        test_input = ""
        TEST = "Test 2"

        expected_amount_of_sentence = 0
        self.assertEqual(expected_amount_of_sentence, get_sentences_amount(test_input),
                         f'incorrect sentences amount {TEST}')

    def test_amount_of_non_declarative_sentence_2(self):
        test_input = ""
        TEST = "Test 2"

        expected_amount_of_non_declarative_sentence = 0

        self.assertEqual(expected_amount_of_non_declarative_sentence,
                         get_not_declarative_sentences_amount(test_input),
                         f'incorrect non declarative sentences amount {TEST}')

    def test_average_length_of_sentence_2(self):
        test_input = ""
        TEST = "Test 2"

        expected_average_length_of_sentence = 0

        self.assertEqual(expected_average_length_of_sentence, get_average_sentence_length(test_input),
                         f'incorrect average length of sentence {TEST}')

    def test_average_length_of_word_2(self):
        test_input = ""
        TEST = "Test 2"

        expected_average_length_of_word = 0

        self.assertEqual(expected_average_length_of_word, get_average_word_length(test_input),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_ngrams_2(self):
        test_input = ""
        TEST = "Test 2"

        K = 10
        N = 2

        expected_K_NGrams = []

        self.assertEqual(expected_K_NGrams, n_grams(test_input, N, K),
                         f'incorrect average length of the word {TEST}')

    # Third test block

    def test_amount_of_sentence_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"

        expected_amount_of_sentence = 3
        self.assertEqual(expected_amount_of_sentence, get_sentences_amount(test_input),
                         f'incorrect sentences amount {TEST}')

    def test_amount_of_non_declarative_sentence_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"

        expected_amount_of_non_declarative_sentence = 2

        self.assertEqual(expected_amount_of_non_declarative_sentence,
                         get_not_declarative_sentences_amount(test_input),
                         f'incorrect non declarative sentences amount {TEST}')

    def test_average_length_of_sentence_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"

        expected_average_length_of_sentence = 9

        self.assertEqual(expected_average_length_of_sentence, get_average_sentence_length(test_input),
                         f'incorrect average length of sentence {TEST}')

    def test_average_length_of_word_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"
        expected_average_length_of_word = 5

        self.assertEqual(expected_average_length_of_word, get_average_word_length(test_input),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_ngrams_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"

        K = 10
        N = 4

        expected_K_NGrams = [('abcd and abcvkdr aaaaaaaa', 1), ('and abcvkdr aaaaaaaa abdc', 1)]

        self.assertEqual(expected_K_NGrams, n_grams(test_input, N, K),
                         f'incorrect average length of the word {TEST}')