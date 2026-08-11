class Solution(object):
    def missingInteger(self, nums):
        c=nums[0]
        r=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i]==c+i:
                r+=nums[i]
            else:
                break
        while True:
            if r in list(nums):
                r+=1
            else:
                return r
