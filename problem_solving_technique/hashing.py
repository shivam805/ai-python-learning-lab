def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    return groups


if __name__ == "__main__":
    print(first_non_repeating_char("aabbcde"))
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
