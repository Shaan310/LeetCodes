class Solution(object):
    def findWordsContaining(self, words, x):
        c=[]
        for i in range(len(words)):
            for wr in words[i]:
                if wr==x:
                    c.append(i)
                    break
        return c
        