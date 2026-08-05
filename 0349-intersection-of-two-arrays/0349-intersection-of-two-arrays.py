class Solution(object):
    def intersection(self, nums1, nums2):
        s=set(nums1)
        c=set()
        for i in range(len(nums2)):
            if nums2[i] not in c:
                if nums2[i] in s:
                    c.add(nums2[i])
        return list(c)


        