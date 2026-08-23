class Solution(object):
    def sortColors(self, nums):
        a=0
        c=0
        while a<=2:
            for i in range(len(nums)):
                if nums[i]==a:
                    nums[c],nums[i]=nums[i],nums[c]
                    c+=1
            a+=1


                    

