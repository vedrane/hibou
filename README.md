# Hibou

A tool for basic textual analysis that provides data on readability, lexical diversity, sentiment analysis, and insights on the text.

To use, run:
`python main.py [filename].txt`
or `hibou [filename].txt`

Results for Fyodor Dostoyevsky's *Crime and Punishment*:
```
RESULTS
----------------
DATA
Total Characters:                        885153
Total Words:                             226356
Total Sentences:                         12021
Total Syllables (Heuristic):             335975
Total Syllables (NLTK):                  292091

AVERAGES
Average Word Length:                     4.02
Average Words per Sentence:              18.83

READABILITY
Automated Readability Index (ARI):       8
Coleman-Liau Index:                      6
Flesch Reading-Ease Score (FRES):        78.55
Flesch-Kincaid Grade Level (FKGL):       6.98

LEXICAL DIVERSITY
Average Word Frequency (AWF):            20.0
Type-Token Ratio (TTR):                  0.05
Corrected Type-Token Ratio (CTTR):       16.96
Log Type-Token Ratio (LTTR):             0.76
Root Type-Token Ratio (RTTR):            23.98
Mass a2:                                 0.05
Summer's Index (S):                      0.83
Uber index (U):                          22.1

SENTIMENT ANALYSIS (VADER)
Positive Sentiment:                      0.11
Neutral Sentiment:                       0.78
Negative Sentiment:                      0.11
Compound Sentiment:                      -1.0

INSIGHTS
For a Flesch reading-ease score (FRES) of 78.55, this text is considered: Easy to read. Conversational English for consumers. Can be read by students in the 6th grade.
For an Automated Readability Index (ARI) of 8, this text is best understood by: Seventh Grade (12-13).
For a Type-Token Ratio of 5.0%, there is a low lexical diversity (high word repetition, limited vocabulary). However, this and other metrics are dependent on the length of the text.
The text is generally neutral to a very high extent.

TIME
49.02 seconds
```