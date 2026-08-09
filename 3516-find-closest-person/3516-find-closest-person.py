class Solution(object):
    def findClosest(self, x, y, z):
        one=abs(x-z)
        two=abs(z-y)
        if one==two:
            return 0 
        elif one<two:
            return 1 
        else:
            return 2 
        