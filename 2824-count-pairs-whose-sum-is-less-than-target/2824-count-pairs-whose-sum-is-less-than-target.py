class Solution(object):
    def countPairs(self, nums, target):
        j=1
        c=0
        n=len(nums)
        for i in range(len(nums)):
            j=i+1
            while j<n:
                if nums[i]+nums[j]<target:
                    c+=1
                j+=1
        return c

        