"""
Написать функцию, выводящую анаграммы переданной строки, содержащиеся в переданном списке строк.
"""

from collections import Counter


def get_anagrams(search_word: str, words_list: list[str]) -> list[str]:
    """
        Function to find all anagrams for search_word found in words_list:
        Examples:
            f('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
    """
    search_word_counter = Counter(search_word)
    anagrams = set()

    for word in words_list:
        if Counter(word) == search_word_counter:
            anagrams.add(word)

    return list(anagrams)


# tests
if __name__ == '__main__':
    print(get_anagrams('abba', ['aabb', 'abbba', 'bba', 'aabb', 'abcd', 'bbaa', 'dada']))
