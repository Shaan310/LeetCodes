class Solution(object):
    def destCity(self, paths):
        n=len(paths)
        s=set()
        for i in range(n):
            s.add(paths[i][0])
        for i in range(n):
            if paths[i][1] not in s:
                return paths[i][1]

        