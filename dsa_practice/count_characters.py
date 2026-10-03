"""Character frequency counting.

This script counts how many times each character appears in a string using a
dictionary. It is a common hashing-based problem in DSA and interview practice.
"""


def count_characters(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


if __name__ == "__main__":
    result = count_characters("programming")
    print(result)
