class Solution(object):
    def majorityElement(self, nums):
        cand = 0
        count = 0
        for num in nums:
            if count == 0:
                cand=num
            if cand==num:
                count+=1
            else: 
                count-=1
        return cand



        