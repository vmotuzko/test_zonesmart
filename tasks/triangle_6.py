"""
На вход подаются целочисленные координаты трех точек на плоскости.
Написать функцию, выводящую координаты всех точек, имеющих целочисленные координаты и лежащих внутри треугольника,
образованного тремя точками.
"""


def find_all_points_inside_triangle(
        p1: tuple[int, int],
        p2: tuple[int, int],
        p3: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Find all integer point inside given triangle
    Example:
        f((2,1), (0,3), (5,4)) => [
            (0,3),
            (1, 2),
            (1, 3),
            (2,1),
            (2, 2),
            (2, 3),
            (3, 2),
            (3, 3),
            (4, 3),
            (5, 4),
        ]

    """

    def is_inside_triangle(p, p1, p2, p3):
        alpha = ((p2[1] - p3[1]) * (p[0] - p3[0]) + (p3[0] - p2[0]) * (p[1] - p3[1])) \
                / ((p2[1] - p3[1]) * (p1[0] - p3[0]) + (p3[0] - p2[0]) * (p1[1] - p3[1]))
        beta = ((p3[1] - p1[1]) * (p[0] - p3[0]) + (p1[0] - p3[0]) * (p[1] - p3[1])) \
               / ((p2[1] - p3[1]) * (p1[0] - p3[0]) + (p3[0] - p2[0]) * (p1[1] - p3[1]))
        gamma = 1 - alpha - beta

        return alpha >= 0 and beta >= 0 and gamma >= 0

    min_x = min(p1[0], p2[0], p3[0])
    max_x = max(p1[0], p2[0], p3[0])
    min_y = min(p1[1], p2[1], p3[1])
    max_y = max(p1[1], p2[1], p3[1])

    points_inside = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            p = (x, y)
            if is_inside_triangle(p, p1, p2, p3):
                points_inside.append(p)

    return points_inside


# tests
if __name__ == '__main__':
    print(find_all_points_inside_triangle((2, 1), (0, 3), (5, 4)))
