class Solution(object):
    def maxArea(self, height):
        r=len(height)
        a=0
        b=r-1
        m=0
        while b>a:                
            if height[a]>=height[b]:
                m=max(height[b]*(b-a),m)
                b-=1
            else:
                m=max(height[a]*(b-a),m)
                a+=1
        return m   
