class Solution(object):
    def numIdenticalPairs(self, nums):
        arr = nums
        r = 0
        n = len(arr)
        for i in range(n):
            for j in range(n - 1, i, -1):
                if arr[i]==arr[j]:
                    r+=1
        return r
        
        