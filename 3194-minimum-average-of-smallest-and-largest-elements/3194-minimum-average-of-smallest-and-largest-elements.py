class Solution(object):
    def minimumAverage(self, nums):
        c=[]
        n=len(nums)
        while len(c)!=n:
            if len(nums)==0:
                return min(c)
            l=(max(nums)+min(nums))/2.00000
            c.append(l)
            nums.remove(max(nums))
            nums.remove(min(nums))
   
        