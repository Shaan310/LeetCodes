class Solution(object):
    def numberOfBeams(self, bank):
        ans=0
        cur=0
        nex=0
        for br in bank:
            for b in br:
                if b=="1":
                    nex+=1
            ans+=(cur*nex)
            if nex > 0:
                cur=nex
                nex=0
        return ans
                

        