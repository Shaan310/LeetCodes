class Solution(object):
    def removeElement(self, nums, val):
        p=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[i],nums[p]=nums[p],nums[i]
                p+=1
        return p

        