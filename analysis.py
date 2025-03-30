import re

def heuristic_syllable_count(word):
    word = word.lower()

    # Words that need syllable adjustments
    exception_add = {'serious', 'crucial'}
    exception_del = {'fortunately', 'unfortunately'}

    co_one = {'cool', 'coach', 'coat', 'coal', 'count', 'coin', 'coarse', 'coup', 'coif', 
              'cook', 'coign', 'coiffe', 'coof', 'court', 'could'}
    co_two = {'coapt', 'coed', 'coinci'}
    pre_one = {'preach'}

    add = 0  # Added syllables
    disc = 0  # Discarded syllables

    # (1) Short words have at least 1 syllable
    if len(word) <= 3:
        return 1

    # (2) Remove silent 'e' at the end
    if word.endswith("e"):
        disc += 1

    # (3) Handle "-es" and "-ed" endings (except special cases)
    if word.endswith(("es", "ed")) and not re.search(r"(ted|tes|ses|ied|ies)$", word):
        if len(re.findall(r'[aeiou][^aeiou]', word)) > 1:
            disc += 1

    # (4) Handle vowel groups (e.g., "rain" should count as 1 syllable)
    disc += len(re.findall(r'[aeiou]{2,}', word))  # Reduce consecutive vowels

    # (5) Count vowels
    vowels = len(re.findall(r'[aeiouy]', word))

    # (6) Special case: "mc-" adds a syllable
    if word.startswith("mc"):
        add += 1

    # (7) Handle "y" at the end (e.g., "happy")
    if word.endswith("y") and word[-2] not in "aeiou":
        add += 1

    # (8) Handle "y" between consonants
    add += sum(1 for m in re.finditer(r'[^aeiou]y[^aeiou]', word))

    # (9) Prefix "tri-" and "bi-" add a syllable if followed by a vowel
    if re.match(r'tri[aeiou]', word) or re.match(r'bi[aeiou]', word):
        add += 1

    # (10) "ian", "ion", "iun" should be counted as 2 syllables, except after "t" or "c"
    add += len(re.findall(r'(?<![tc])i[ao]n|(?<![tc])iun', word))

    # (11) Handle "co-" prefix rules
    if word.startswith("co") and word[2] in "aeiou":
        if any(word.startswith(x) for x in co_two):
            add += 1
        elif not any(word.startswith(x) for x in co_one):
            add += 1

    # (12) Handle "pre-" prefix rules
    if word.startswith("pre") and word[3] in "aeiou":
        if not any(word.startswith(x) for x in pre_one):
            add += 1

    # (13) Handle "-n't" contractions
    if word.endswith("n't") and word[-4] not in "aeiou":
        add += 1

    # (14) Handle exceptions
    if word in exception_del:
        disc += 1
    if word in exception_add:
        add += 1

    # Calculate final syllable count
    return max(1, (vowels - disc) + add)