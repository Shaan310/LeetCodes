class Solution(object):
    def sortPeople(self, names, heights):
        c=0
        while c<len(names):
            b=max(heights[c:])
            for i in range(c,len(names)):
                if heights[i]==b:
                    names[c],names[i]=names[i],names[c]
                    heights[c],heights[i]=heights[i],heights[c]
                    c+=1
                    break
        return names


        