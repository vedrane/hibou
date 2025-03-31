fres_insights = [
    "Extremely difficult to read. Best understood by professionals.",
    "Very difficult to read. Can be read by college graduates.",
    "Difficult to read. Can be read by college students.",
    "Fairly difficult to read. Can be read by students in the 10th-12th grade.",
    "Plain English. Easily understood by 13- to 15-year-old students. Can be read by students in the 8th-9th grade.",
    "Fairly easy to read. Can be read by students in the 7th grade.",
    "Easy to read. Conversational English for consumers. Can be read by students in the 6th grade.",
    "Very easy to read. Easily understood by an average 11-year-old student. Can be read by students in the 5th grade.",
    "Extremely easy to read. Can be read by most English speakers."
]

ari_insights = [
    "Anyone",
    "Kindergarten (5-6)",
    "First Grade (6-7)",
    "Second Grade (7-8)",
    "Third Grade (8-9)",
    "Fourth Grade (9-10)",
    "Fifth Grade (10-11)",
    "Sixth Grade (11-12)",
    "Seventh Grade (12-13)",
    "Eighth Grade (13-14)",
    "Ninth Grade (14-15)",
    "Tenth Grade (15-16)",
    "Eleventh Grade (16-17)",
    "Twelfth Grade (17-18)",
    "College Student (18-22)",
    "Professional (22+)"
]

def readability_insights(ari, fres):
    if fres < 0:
        f = fres_insights[0]
    elif fres < 10:
        f = fres_insights[1]
    elif fres < 30:
        f = fres_insights[2]
    elif fres < 50:
        f = fres_insights[3]
    elif fres < 60:
        f = fres_insights[4]
    elif fres < 70:
        f = fres_insights[5]
    elif fres < 80:
        f = fres_insights[6]
    elif fres < 90:
        f = fres_insights[7]
    else:
        f = fres_insights[8]

    if ari < 1:
        a = ari_insights[0]
    elif ari > 14:
        a = ari_insights[15]
    else:
        a = ari_insights[int(ari)]

    return f"For a Flesch reading-ease score (FRES) of {fres}, this text is considered: {f}\nFor an Automated Readability Index (ARI) of {ari}, this text is best understood by: {a}."

def lexical_diversity_insights(ttr):
    if ttr >= 0.7:
        l = "very high lexical diversity (rich vocabulary, few repeated words)"
    elif ttr >= 0.5:
        l = "moderate lexical diversity (some repetition, but still varied)"
    else:
        l = "low lexical diversity (high word repetition, limited vocabulary)"
    
    return f"For a Type-Token Ratio of {ttr * 100}%, there is a {l}. However, this and other metrics are dependent on the length of the text."

def sentiment_insights(pos, neg, neu):
    def extent(score):
        if score >= 0.75:
            return "very high"
        elif score >= 0.5:
            return "moderate"
        elif score >= 0.25:
            return "low"
        else:
            return "very low"
    if pos > neg:
        if pos > neu:
            return f"The text is generally positive, to a {extent(pos)} extent."
        else:
            return f"The text is generally neutral to a {extent(neu)} extent."
    elif neg > neu:
        return f"The text is generally negative to a {extent(neg)} extent."
    else:
        return f"The text is generally neutral to a {extent(neu)} extent."