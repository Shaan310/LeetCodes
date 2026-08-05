class Solution(object):
    def majorityElement(self, nums):
        s={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in s:
                s[nums[i]]=1
            else:
                s[nums[i]]+=1
        for key,value in s.items():
            if value>(n/2):
                return key



        