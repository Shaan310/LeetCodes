class Solution(object):
    def concatWithReverse(self, nums):
        rev=nums[::-1]
        ans= nums+rev
        return ans
        