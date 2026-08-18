class Solution(object):
    def largestInteger(self, nums, k):
        d={}
        c=-1
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        if k==1:
            for key,value in d.items():
                if value==1:
                    if key>c:
                        c=key
            return c
        if k==n:
            return max(nums)
        if d[nums[0]]>1 and d[nums[-1]]>1:
            return c
        elif d[nums[0]]>1:
            return nums[-1]
        elif d[nums[-1]]>1:
            return nums[0]
        else:
            return max(nums[0],nums[-1])



        
        

        
        