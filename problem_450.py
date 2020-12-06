"""
You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""


def is_balanced(string: str) -> bool:
    unmatched: int = 0
    generics: int = 0
    for character in string:
        if character == '(':
            unmatched += 1
        elif character == ')':
            unmatched -= 1
            generics = 0
        elif character == '*':
            generics += 1

        if unmatched < 0:
            break

    return unmatched == 0 or (unmatched == generics)


if __name__ == '__main__':
    print(is_balanced('((((****'))
