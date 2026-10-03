def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))


def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())


if __name__ == "__main__":
    print(reverse_words("Python is fun"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_anagram("listen", "silent"))
