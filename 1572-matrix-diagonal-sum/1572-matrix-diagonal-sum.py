class Solution(object):
    def diagonalSum(self, mat):
        n=len(mat)
        c=0
        r=n-1
        p=0
        for i in range(n):
            if (p+i)==(r-i):
                c+=mat[p+i][p+i]
            else:
                c+=(mat[p+i][p+i]+mat[i][r-i])
        return c


        