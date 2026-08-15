class Solution(object):
    def recoverOrder(self, order, friends):
        c=[]
        fr=set(friends)
        for o in order:
            if o in fr:
                c.append(o)
        return c
        