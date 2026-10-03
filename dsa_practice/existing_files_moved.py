"""Legacy practice solutions grouped in one file.

This file contains earlier implementations that were originally kept as separate
root files. It is kept here for reference and consolidation into a single DSA
practice folder.
"""

# This file keeps the original practice files together in one place.
# You can move or rename these later as needed.

# binary_search.py

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(binary_search([1, 3, 5, 7, 9, 11], 7))

# count_char.py

def char_frequency(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq


print(char_frequency("programming"))

# find_dup.py

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


print(find_duplicates([1, 2, 3, 2, 4, 5, 1, 3]))

# reverse_str.py

def reverse_string(s):
    result = ""

    for i in range(len(s) - 1, -1, -1):
        result += s[i]

    return result


print(reverse_string("Python"))

# second_larg.py

def second_largest(arr):
    largest = float("-inf")
    second = float("-inf")

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second


print(second_largest([10, 5, 20, 8, 20, 15]))
