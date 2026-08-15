class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        a=abs(ax1-ax2)*abs(ay1-ay2)
        b=abs(bx1-bx2)*abs(by1-by2)
        cx1=max(ax1,bx1)
        cy1=max(ay1,by1)
        cx2=min(ax2,bx2)
        cy2=min(ay2,by2)
        c=abs(cx1-cx2)*abs(cy1-cy2)
        c=max(0,cx2-cx1)*max(0,cy2-cy1)
        return a+b-c