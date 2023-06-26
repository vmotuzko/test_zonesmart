"""
Написать функцию, которая обходит все элементы двумерной матрицы по часовой стрелке снаружи внутрь
(по спирали от верхнего левого элемента), выводя числа внутри элементов.
"""

from typing import Optional


def traverse_matrix_spiral(matrix=list[list[int]]) -> Optional[list]:
    """
        Traverse given matrix in spiral clockwise sequence
        Examples:
             m = [
                    [1,2,3,1],
                    [4,5,6,4],
                    [7,8,9,7],
                    [7,8,9,7]
                ]
                f(m) => [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]
    """
    if len(matrix) == 0:
        return
    result = matrix.pop(0)
    next_step = traverse_matrix_spiral([list(x) for x in list(zip(*matrix))][::-1])
    if next_step is not None:
        return result + next_step
    return result


if __name__ == '__main__':
    print(traverse_matrix_spiral(
        [
            [1, 2, 3, 1],
            [4, 5, 6, 4],
            [7, 8, 9, 7],
            [7, 8, 9, 7]
        ]
    ))
