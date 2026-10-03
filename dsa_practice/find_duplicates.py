"""Duplicate detection in a list.

This script finds repeated numbers using a set to track seen elements. It is a
classic beginner problem that demonstrates hash-based lookup.
"""

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 5, 5, 6]))
