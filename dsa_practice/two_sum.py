"""Two-sum problem using a hash map.

This script finds the indices of two numbers in an array that sum to a target.
It uses a dictionary to store seen values and efficiently check complements.
"""

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
