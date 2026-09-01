class Solution(object):
    def findWordsContaining(self, words, x):
        c=[]
        for i in range(len(words)):
            if x in words[i]:
                c.append(i)
        return c
        
        