"""Merge two sorted arrays.

This script combines two sorted lists into one sorted list using a two-pointer
approach. It is a classic problem that demonstrates efficient merge logic.
"""

def merge_sorted_arrays(a, b):
    merged = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


if __name__ == "__main__":
    print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
