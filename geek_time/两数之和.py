def two_sum(nums, target):
    hash_map = {}
    for index, num in enumerate(nums):
        hash_map[num] = index
    for i, num in enumerate(nums):
        j = hash_map.get(target - num)
        if j is not None and i != j:
            return [i, j]
