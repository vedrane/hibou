# Hibou

A tool for basic textual analysis that provides data on readability, lexical diversity, and sentiment analysis and summarizes the text (TODO).

To use, run:
`python main.py example.txt`

Example text taken from Thomas Hobbes' *The Leviathan*, Part I, Chapter I. The results from running the program on it:
```
DATA
Total Characters:                        3068
Total Words:                             714
Total Sentences:                         20
Total Syllables (Heuristic):             1157
Total Syllables (NLTK):                  1007

READABILITY
Automated Readability Index (ARI):       16.8
Coleman-Liau Index:                      8.64
Flesch Reading-Ease Score (FRES):        51.28
Flesch-Kincaid Grade Level (FKGL):       14.98

LEXICAL DIVERSITY
Type-Token Ratio (TTR):                  0.39
Corrected Type-Token Ratio (CTTR):       7.46
Log Type-Token Ratio (LTTR):             0.86
Root Type-Token Ratio (RTTR):            10.55

SENTIMENT ANALYSIS (VADER)
Positive Sentiment:                      0.05
Neutral Sentiment:                       0.932
Negative Sentiment:                      0.018
Compound Sentiment:                      0.9602
```
