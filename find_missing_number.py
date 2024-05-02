def find_missing_number(nums):
    if len(nums) >= 1:
        nums.sort()

        for ele in range(max(nums) + 2):
            if ele not in nums:
                return ele
    else:
        return 0


print(find_missing_number([]))
