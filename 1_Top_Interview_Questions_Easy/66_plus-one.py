class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] %= 10
                flag = 1
            else:
                flag = 0
            if flag == 0 :
                break
        if flag != 0:
            digits.insert(0, 1)
        return digits
        

digits = [9,9,9,8]
solution = Solution()
res = solution.plusOne(digits)
print res