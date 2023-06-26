"""
Написать функцию, принимающую на вход список букв и выводящую такую букву, которую можно вставить в список так,
чтобы получился отрывок из английского алфавита (возрастающая последовательность букв без пропусков).
"""

from typing import Optional


def get_missing_letter_or_none(char_sequence: list[str]) -> Optional[str]:
    """
    Function to find only one letter missing in given char_sequence to build ascending english alphabet sequence,
    if given sequence is not valid returns None
    Examples:
        ['a', 'b', 'c', 'd', 'f'] -> 'e'
        ['O', 'Q', 'R', 'S'] -> 'P'
    """
    letter = None
    for i in range(len(char_sequence) - 1):
        diff = ord(char_sequence[i + 1]) - ord(char_sequence[i])
        if diff == 2:
            if letter is None:
                letter = chr(ord(char_sequence[i]) + 1)
            else:
                # we only look for sequence with 1 word gap
                return None
        elif diff > 2 or diff < 1:
            # if we have at least one gap longer than one character or a repetition, it makes no sense for us to look further
            return None
    return letter


# tests
if __name__ == '__main__':
    print(get_missing_letter_or_none(['a', 'b', 'c', 'd', 'f']))
    print(get_missing_letter_or_none(['O', 'Q', 'R', 'S']))
    print(get_missing_letter_or_none(['a', 'b', 'c', 'd', 'f', 'h']))
    print(get_missing_letter_or_none(['A', 'd', 'f', 'h']))
