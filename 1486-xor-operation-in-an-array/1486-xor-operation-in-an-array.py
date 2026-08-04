class Solution(object):
    def xorOperation(self, n, start):
        c=start
        for i in range(1,n):
            c = c^(start + 2 * i)
        return c

        