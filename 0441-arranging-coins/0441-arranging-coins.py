class Solution(object):
    def arrangeCoins(self, n):
        i=1
        while True:
            if n-i<0:
                return i-1
            n=n-i
            i+=1


        