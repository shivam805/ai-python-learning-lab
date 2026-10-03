"""Find the second largest number in a list.

This script identifies the second largest unique or non-unique value in an array
using a single pass. It is a common interview problem for understanding tracking
logic in loops.
"""

def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None


if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 1]))
    print(second_largest([10, 5, 20, 8, 20, 15]))
