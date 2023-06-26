"""
Написать функцию, которая увеличивает на единицу число в конце строки. В строке либо есть единственное число в конце,
либо вовсе нет числа. Если нет числа, то считаем, что строка заканчивается нулем.
Если в числе есть лидирующие нули, то количество цифр не должно меняться.
"""

import re


def increment_number_in_string(word: str) -> str:
    """
    Function to increment number in the end of the given string
    Examples:
        foo -> foo1
        foobar23 -> foobar24
        foo0042 -> foo0043
        foo9 -> foo10
        foo099 -> foo100
    """
    pattern = r'(\d*$)'
    match = re.search(pattern, word)

    if match and match.group(1):
        number = match.group(1)
        incremented_number = str(int(number) + 1).zfill(len(number))
        return word.replace(number, incremented_number)
    else:
        return word + '1'


if __name__ == '__main__':
    print(increment_number_in_string('foo'))
    print(increment_number_in_string('foobar23'))
    print(increment_number_in_string('foo0042'))
    print(increment_number_in_string('foo9'))
    print(increment_number_in_string('foo099'))
