class Solution(object):
    def leftRightDifference(self, nums):
        left=[0]
        right=[0]
        n=len(nums)
        if n==1:
            return [0]
        for i in range(n):
            left.append(left[i]+nums[i])
            if len(left)==n:
                right.append(right[i]+nums[n-i-1])
                break
            right.append(right[i]+nums[n-i-1])
        right.reverse()
        c=[]
        for i in range(n):
            c.append(abs(left[i]-right[i]))
        return c