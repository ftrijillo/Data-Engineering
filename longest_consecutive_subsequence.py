def longest_consecutive_subsequence(nums):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)

    # If the array has only one element, the longest consecutive subsequence is 1
    if n == 1:
        return 1

    # If the array is empty, return 0
    if n == 0:
        return 0

    count = 1
    max_count = -1

    for i in range(n - 1):
        # Check if the difference between the current element and the next element is 1
        if nums[i + 1] - nums[i] == 1:
            count += 1
        # If the difference is 0, continue to the next iteration
        elif nums[i + 1] - nums[i] == 0:
            continue
        # If the difference is not 1 or 0, reset the count to 1
        else:
            count = 1

        # Update max_count with the maximum value between max_count and count
        max_count = max(max_count, count)

    return max_count


print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))
