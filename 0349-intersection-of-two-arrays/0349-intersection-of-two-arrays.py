class Solution(object):
    def intersection(self, nums1, nums2):
        s=set(nums1)
        c=[]
        for i in range(len(nums2)):
            if nums2[i] not in c:
                if nums2[i] in s:
                    c.append(nums2[i])
        return c


        