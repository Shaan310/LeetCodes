class Solution(object):
    def flipAndInvertImage(self, image):
        c = [row[::-1] for row in image]
        for i in range(len(c)):
            for j in range(len(c[i])):
                if c[i][j]==0:
                    c[i][j]=1
                else:
                    c[i][j]=0
        return c
                
        