class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        this_i = 0
        tag = 1
        for i in range(1, len(nums)):
            if nums[this_i] < nums[i]:
                temp = nums[tag]
                nums[tag] = nums[i]
                nums[i] = nums[tag]
                this_i = tag
                tag += 1
        return this_i + 1

nums = [0,0,1,1,1,2,2,3,3,4,4]

solution = Solution()
res = solution.removeDuplicates(nums)
print res