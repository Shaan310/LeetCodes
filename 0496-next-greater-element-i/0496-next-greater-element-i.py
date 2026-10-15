class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums2)
        c=[]
        s={}
        for i in range(n):
            s[nums2[i]]=i
        for no in nums1:
            r=s[no]
            for i in range(r+1,n):
                if nums2[i] > no:
                    c.append(nums2[i])
                    break
            else:
                c.append(-1)
        return c
                

                



        