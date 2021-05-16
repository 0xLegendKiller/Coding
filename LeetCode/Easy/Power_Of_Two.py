class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1: return False
        while n%2==0: n=n/2
        return n==1
      
# This works but exceeds waiting/judging time 
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = 0
        for i in range(0, n):
            if n == 2 ** i:
                flag = 1
            else:
                continue
        if flag == 1:
            return True
        else:
            return False
'''
