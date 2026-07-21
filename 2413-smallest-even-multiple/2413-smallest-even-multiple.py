class Solution(object):
    def smallestEvenMultiple(self, n):
        if n>=1:
            if (n%2==0):
                r=n
            else:
                r=n*2
            return r

        
        