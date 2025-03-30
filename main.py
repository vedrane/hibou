import math
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, SyllableTokenizer
from nltk.corpus import cmudict
from nltk.sentiment import SentimentIntensityAnalyzer
from analysis import heuristic_syllable_count
from readability import flesch_reading_ease, flesch_kincaid_grade, automated_readability_index, coleman_liau_index

nltk.download('punkt', quiet=True)
nltk.download('cmudict', quiet=True)
nltk.download('vader_lexicon', quiet=True)
d = cmudict.dict()
sid = SentimentIntensityAnalyzer()

text = "The Australian platypus is seemingly a hybrid of a mammal and reptilian creature."
chars = len(re.findall(r'[a-zA-Z0-9]', text))
sentences = len(sent_tokenize(text))

words = word_tokenize(text)
words = [word for word in words if not word in ['.', ',', '!', '?']]
num_words = len(words)

def count_syllables(word):
    word = word.lower()
    if word in d:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word]][0]
    return 1

syllables = sum([count_syllables(word) for word in words])
sentiment_score = sid.polarity_scores(text)

types = len(set(words))
tokens = num_words


print("RESULTS\n----------------")
print("DATA")
print("Total Characters:\t\t\t", chars)
print("Total Words:\t\t\t\t", num_words)
print("Total Sentences:\t\t\t", sentences)
print("Total Syllables (Heuristic):\t\t", heuristic_syllable_count(text))
print("Total Syllables (NLTK):\t\t\t", syllables)

print("\nREADABILITY")
print("Automated Readability Index (ARI):\t", automated_readability_index(text, chars, sentences))
print("Coleman-Liau Index:\t\t\t", coleman_liau_index(chars, num_words, sentences))
print("Flesch Reading-Ease Score (FRES):\t", flesch_reading_ease(text, words, num_words, sentences, syllables))
print("Flesch-Kincaid Grade Level (FKGL):\t", flesch_kincaid_grade(text, words, num_words, sentences, syllables))

print("\nLEXICAL DIVERSITY")
print("Type-Token Ratio (TTR):\t\t\t", round((types / tokens), 2))
print("Corrected Type-Token Ratio (CTTR):\t", round((types / math.sqrt(2 * tokens)), 2))
print("Log Type-Token Ratio (LTTR):\t\t", round((math.log10(types) / math.log10(tokens)), 2))
print("Root Type-Token Ratio (RTTR):\t\t", round((types / math.sqrt(tokens)), 2))

print("\nSENTIMENT ANALYSIS (VADER)")
print("Positive Sentiment:\t\t\t", sentiment_score['pos'])
print("Neutral Sentiment:\t\t\t", sentiment_score['neu'])
print("Negative Sentiment:\t\t\t", sentiment_score['neg'])
print("Compound Sentiment:\t\t\t", sentiment_score['compound'])