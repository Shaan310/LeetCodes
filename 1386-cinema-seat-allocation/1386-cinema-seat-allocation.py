class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        s={}
        for row, seat in reservedSeats:
            if row not in s:
                s[row] = set()
            s[row].add(seat)
        c=(n-len(s))*2

        for row in s:
            seats = s[row]
            l=not({2,3,4,5} & seats)
            m=not({4,5,6,7} & seats)
            r=not({6,7,8,9} & seats)
            if l and r:
                c+= 2
            elif l or m or r:
                c+= 1
        return c
