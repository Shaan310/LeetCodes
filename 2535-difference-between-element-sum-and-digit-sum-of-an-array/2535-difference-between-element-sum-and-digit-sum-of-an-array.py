class Solution(object):
    def differenceOfSum(self, nums):
        e=0
        s=0
        r=0
        for num in nums:
            if num>9:
                e+=num
                while num>0:
                    r=num%10
                    s+=r
                    num=num//10
            else:
                e+=num
                s+=num
        return abs(e-s)


        