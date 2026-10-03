"""String-based problem-solving examples.

This file contains common interview-style questions involving string operations,
including reversing words, checking anagrams, and finding the longest palindrome
substring.
"""


def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))


def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())


def longest_palindrome_substring(s):
    if not s:
        return ""
    best = s[0]
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best


if __name__ == "__main__":
    print(reverse_words("Python is fun"))
    print(is_anagram("listen", "silent"))
    print(longest_palindrome_substring("babad"))
