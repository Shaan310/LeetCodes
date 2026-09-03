class Solution(object):
    def numberGame(self, nums):
        c=[]
        n=len(nums)
        while n>=2:
            
            a=min(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            c.append(b)
            c.append(a)
            n=len(nums)
        return c

        