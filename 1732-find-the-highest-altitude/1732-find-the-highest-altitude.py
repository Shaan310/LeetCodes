class Solution(object):
    def largestAltitude(self, gain):
        c=0
        h=0
        for gai in gain:
            c+=gai

            if c>h:
                h=c
        return h

    
        

        