class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i]==jewels[j]:
                    c+=1
        return c        