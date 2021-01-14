
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index1 = 0
    index2 = 1
    for i in nums:
        for j in nums[1:]:
            if i + j == target:
                return index1, index2
            index2 += 1
        index1 += 1



if __name__ == '__main__':
    a = [3,2,3][1:]
    print(a)
    # print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,3], 6))
