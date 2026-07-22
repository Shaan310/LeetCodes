class Solution(object):
    def singleNumber(self, nums):
        s={}
        for i in range(len(nums)):
            if nums[i] in s:
                s[nums[i]]+=1
            else:
                s[nums[i]]=1
        for key, value in s.items():
            if value == 1:
                return key
                
        