class Solution(object):
    def twoSum(self, nums, target):
        arr =  nums
        seen = {}
        for i in range(len(arr)):
            need = target - arr[i]
            if need in seen:
                return [seen[need],i]
            else:
                seen[nums[i]]=i
        