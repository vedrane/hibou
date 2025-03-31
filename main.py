import re
import sys
import time
from math import sqrt, log10

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, SyllableTokenizer
from nltk.corpus import cmudict
from nltk.sentiment import SentimentIntensityAnalyzer

from analysis import average_word_length, average_word_per_sentence, heuristic_syllable_count
from readability import flesch_reading_ease, flesch_kincaid_grade, automated_readability_index, coleman_liau_index
from insights import readability_insights, lexical_diversity_insights, sentiment_insights

nltk.download('punkt', quiet=True)
nltk.download('cmudict', quiet=True)
nltk.download('vader_lexicon', quiet=True)
d = cmudict.dict()
sid = SentimentIntensityAnalyzer()


if len(sys.argv) >= 2:
    arg = sys.argv[1]
elif(len(sys.argv) == 1 and sys.argv[0] != 'main.py'):
    argv = sys.argv[0]
else:
    print("Usage: hibou [file]\n       python main.py [file]")
    sys.exit(1)

try:
    with open(arg, 'r', encoding='utf-8') as file:
        text = file.read().strip()
        if(text):
            start = time.time()
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
            ttr = round((types / tokens), 2)

            ari = automated_readability_index(text, chars, sentences)
            cli = coleman_liau_index(chars, num_words, sentences)
            fkgl = flesch_kincaid_grade(text, words, num_words, sentences, syllables)
            fres = flesch_reading_ease(text, words, num_words, sentences, syllables)

            print("RESULTS\n----------------")
            print("DATA")
            print("Total Characters:\t\t\t", chars)
            print("Total Words:\t\t\t\t", num_words)
            print("Total Sentences:\t\t\t", sentences)
            print("Total Syllables (Heuristic):\t\t", heuristic_syllable_count(text))
            print("Total Syllables (NLTK):\t\t\t", syllables)

            print("\nAVERAGES")
            print("Average Word Length:\t\t\t", average_word_length(words))
            print("Average Words per Sentence:\t\t", average_word_per_sentence(words, sentences))

            print("\nREADABILITY")
            print("Automated Readability Index (ARI):\t", ari)
            print("Coleman-Liau Index:\t\t\t", cli)
            print("Flesch Reading-Ease Score (FRES):\t", fres)
            print("Flesch-Kincaid Grade Level (FKGL):\t", fkgl)

            print("\nLEXICAL DIVERSITY")
            print("Average Word Frequency (AWF):\t\t", round(1/ttr, 2))
            print("Type-Token Ratio (TTR):\t\t\t", ttr)
            print("Corrected Type-Token Ratio (CTTR):\t", round((types / sqrt(2 * tokens)), 2))
            print("Log Type-Token Ratio (LTTR):\t\t", round((log10(types) / log10(tokens)), 2))
            print("Root Type-Token Ratio (RTTR):\t\t", round((types / sqrt(tokens)), 2))
            print("Maas a2:\t\t\t\t", round((((log10(tokens) - log10(types)) / log10(tokens)**2)), 2))
            print("Summer's Index (S):\t\t\t", round((log10(log10(types)) / log10(log10(tokens))), 2))
            print("Uber index (U):\t\t\t\t", round(((log10(tokens)**2) / (log10(tokens) - log10(types))), 2))

            print("\nSENTIMENT ANALYSIS (VADER)")
            print("Positive Sentiment:\t\t\t", round(sentiment_score['pos'], 2))
            print("Neutral Sentiment:\t\t\t", round(sentiment_score['neu'], 2))
            print("Negative Sentiment:\t\t\t", round(sentiment_score['neg'], 2))
            print("Compound Sentiment:\t\t\t", round(sentiment_score['compound'], 2))

            print("\nINSIGHTS")
            print(readability_insights(ari, fres))
            print(lexical_diversity_insights(ttr))
            print(sentiment_insights(sentiment_score['pos'], sentiment_score['neg'], sentiment_score['neu']))

            print("\nTIME")
            print(round(time.time() - start, 2), "seconds")

except FileNotFoundError:
    print(f"Error: File not found.")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)