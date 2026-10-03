"""Array problem-solving examples.

This file contains a few beginner-friendly array exercises:
- maximum subarray sum
- rotating an array
- checking for duplicates

Each function is implemented with simple Python logic and can be used as a
reference for interview and DSA practice.
"""


def max_subarray_sum(nums):
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


def rotate_array(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(rotate_array([1, 2, 3, 4, 5], 2))
    print(contains_duplicate([1, 2, 3, 4, 2]))
