class Solution(object):
    def largestAltitude(self, gain):
        alt=[]
        c=0
        alt.append(c)
        for gai in gain:
            c+=gai
            alt.append(c)
        return max(alt)
        

        