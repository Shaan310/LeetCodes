class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x-z)==abs(z-y):
            return 0 
        if abs(x-z)<abs(z-y):
            return 1 
        else:
            return 2 
        