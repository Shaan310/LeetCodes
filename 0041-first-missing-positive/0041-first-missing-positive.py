class Solution(object):
    def firstMissingPositive(self, nums):
        arr = nums
        arr.sort()
        ind=-1
        for i in range(len(arr)):
            if arr[i]<=0:
                continue
            if arr[i] > 0:
                ind = i
                break
        if ind==-1:
                return 1     


        if arr[ind]!=1:
            return(1)
        else:
            one = 1
            for j in range(ind,len(arr)):
                if arr[j] == one:
                    one += 1
                elif arr[j] < one:
                    continue
                elif arr[j] > one:
                    return one
            return one    