"""Palindrome checker.

This script checks whether a string is a palindrome while ignoring case and
non-alphanumeric characters. It is a common string-processing interview question.
"""

def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("hello"))
