class Solution:
    def leftRightDifference(self, nums):
        right=sum(nums)
        left=0
        c=[]
        for num in nums:
            right-=num
            c.append(abs(left-right))
            left+=num
        return c
