'''
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_length = len(nums)
    result = []
    if nums_length == 1:
        return sum(nums)
    if nums_length == 2:
        return max([nums[0], nums[1], sum(nums)])
    for item in nums:
        result.append(item)
    for split_length in range(2, nums_length+1):
        start = 0
        end = split_length
        for item in range(0, nums_length):
            result.append(sum(nums[start:end]))
            start += 1
            end += 1
    return max(result)


def max_sub_array(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)

if __name__ == '__main__':
    # print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sub_array([5,4,-1,7,8]))
    # print(maxSubArray([1,-1,1]))
    # print(maxSubArray([5,4,-1,7,8]))

