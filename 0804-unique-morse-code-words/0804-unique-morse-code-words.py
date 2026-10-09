class Solution(object):
    def uniqueMorseRepresentations(self, words):
        c={}
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(97, 123):
            c[chr(i)]=morse[i-97]
        a=[]
        for w in words:
            p=""
            for wi in w:
                p+=c[wi]
            if p not in a:
                a.append(p)
        return len(a)
        