def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


def max_subarray_sum(nums):
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
