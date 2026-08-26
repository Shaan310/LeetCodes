class Solution(object):
    def destCity(self, paths):
        n=len(paths)
        s=set()
        for a,b in paths:
            s.add(a)
        for a,b in paths:
            if b not in s:
                return b 

        