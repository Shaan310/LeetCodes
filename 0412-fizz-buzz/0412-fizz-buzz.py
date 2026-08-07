class Solution(object):
    def fizzBuzz(self, n):
        s=[]
        for i in range(1,n+1):
            if i%15==0:
                s.append("FizzBuzz")
            elif i%5==0:
                s.append("Buzz")
            elif i%3==0:
                s.append("Fizz")
            else:
                s.append(str(i))
        return s

        