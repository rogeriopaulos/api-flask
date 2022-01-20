import re


def count_vowels(word: str) -> int:
    try:
        just_vowels = re.compile(r"[a,e,i,o,u]")
        count = len(just_vowels.findall(word))
    except TypeError:
        count = 0
    return count
