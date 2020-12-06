"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def in_order(a: str, b: str) -> bool:
    return a == 'R' or (a == 'G' and b != 'R') or (a == b == 'B')


def segregate(items: list) -> list:
    ordered: bool = False
    while not ordered:
        i: int = 0
        ordered = True
        while i + 1 < len(items):
            print(items)
            if not in_order(items[i], items[i + 1]):
                items[i], items[i + 1] = items[i + 1], items[i]
                ordered = False

            i += 1

    return items


if __name__ == '__main__':
    print(segregate(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
