class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]

# out of runtime

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
res = solution.twoSum(nums, target)
print res