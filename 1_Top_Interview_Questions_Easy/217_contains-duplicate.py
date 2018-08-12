class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set(nums)
        if len(temp) != len(nums):
        	return True
        else:
        	return False

nums = [1,1,1,3,3,4,3,2,4,2]

solution = Solution()
res = solution.containsDuplicate(nums)

print res