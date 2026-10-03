"""Binary search implementation.

Binary search is a divide-and-conquer algorithm for searching in a sorted array.
It repeatedly compares the target with the middle element and reduces the search
space by half until the value is found or the range is empty.
"""


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(nums, 7))
    print(binary_search(nums, 8))
