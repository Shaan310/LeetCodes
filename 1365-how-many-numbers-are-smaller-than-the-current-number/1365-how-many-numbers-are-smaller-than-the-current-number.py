class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = nums
        n = len(arr)
        count = []
        for i in range(n):
            r=0
            for j in range(n):
                if arr[i]>arr[j]:
                    r+=1
            count.append(r)
        return count


        