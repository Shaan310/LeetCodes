class Solution(object):
    def findNumbers(self, nums):
        arr = nums
        count = 0
        for i in range(len(arr)):
            if (len(str(arr[i]))%2)==0:
                count+=1
        return count

        
        