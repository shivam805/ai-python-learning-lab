"""Hash map-based problem-solving examples.

This file includes common hash map tasks such as:
- finding the first non-repeating character
- grouping anagrams
- solving the two-sum problem using a dictionary
"""


def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


def group_anagrams(words):
    grouped = {}
    for word in words:
        key = ''.join(sorted(word))
        grouped.setdefault(key, []).append(word)
    return list(grouped.values())


def two_sum_hash(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(first_non_repeating_char("aabbcdef"))
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(two_sum_hash([2, 7, 11, 15], 9))
