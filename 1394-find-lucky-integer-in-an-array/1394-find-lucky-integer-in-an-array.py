class Solution(object):
    def findLucky(self, arr):
        s={}
        for i in range(len(arr)):
            if arr[i] not in s:
                s[arr[i]]=1
            else:
                s[arr[i]]+=1
        c=-1
        for key, value in s.items():
            if key==value:
                c=max(key,c)
        return c

        