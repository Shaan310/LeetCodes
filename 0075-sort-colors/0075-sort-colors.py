class Solution(object):
    def sortColors(self, nums):
        a=min(nums)
        b=max(nums)
        c=0
        while a<=b:
            for i in range(len(nums)):
                if nums[i]==a:
                    nums[c],nums[i]=nums[i],nums[c]
                    c+=1
            a+=1


                    

