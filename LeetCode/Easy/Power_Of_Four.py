class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        flag = 0
        for i in range(0, n):
            if n == 4 ** i:
                flag = 1
                break
            else:
                flag = 0
                continue
        if flag == 1:
            return True
        else:
            return False

# c1 = Solution()
# print(c1.isPowerOfFour(16))
