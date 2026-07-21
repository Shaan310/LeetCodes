class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        p=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                nums[p]=nums[i]
                p+=1
        return p
        
        