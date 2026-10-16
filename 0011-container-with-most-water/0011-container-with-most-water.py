class Solution(object):
    def maxArea(self, height):
        r=len(height)
        a=0
        b=r-1
        m=0
        while True:
            if a==b:
                return m
            if height[a]>=height[b]:
                m=max(height[b]*abs(a-b),m)
                b-=1
            else:
                m=max(height[a]*abs(a-b),m)
                a+=1