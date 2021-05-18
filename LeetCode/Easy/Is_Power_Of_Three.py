# this code works but exceeds time limit
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        flag = 0
        for i in range(0, n):
            if n == 3 ** i:
                flag = 1
                break

            else:
                flag = 0
                continue
        if flag == 1:
            return True
        else:
            return False


c1 = Solution()
c1.isPowerOfThree(27)
