import math
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, SyllableTokenizer
from nltk.corpus import cmudict
from analysis import heuristic_syllable_count

def flesch_reading_ease(text, words, num_words, sentences, syllables):
    return round((206.835 - (1.015 * ( num_words / sentences ))) - (84.6 * (syllables / num_words)), 2)

def flesch_kincaid_grade(text, words, num_words, sentences, syllables):
    return round(((0.39 * ( num_words / sentences )) + (11.8 * (syllables / num_words))) - 15.59, 2)

def automated_readability_index(text, chars, sentences):
    text = text.replace('\n', ' ')
    words = len(re.findall(r'\s+', text))
    return math.ceil(((4.71 * (chars / words)) + (0.5 * (words / sentences))) - 21.43)


def coleman_liau_index(chars, words, sentences):
    L = (chars / words) * 100
    S = (sentences / words) * 100

    return math.ceil((0.0588 * L) - (0.296 * S) - 15.8)