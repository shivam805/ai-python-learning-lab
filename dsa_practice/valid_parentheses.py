"""Valid parentheses check.

This script validates whether a string of parentheses is correctly balanced using
stack-based logic. It is a standard problem in DSA and coding interviews.
"""


def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack


if __name__ == "__main__":
    print(is_valid_parentheses("()[]{}"))
    print(is_valid_parentheses("([)]"))
