class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while len(str(num)) != 1:
            for i in str(num):
                res += int(i)
            num = res
            res = 0
            if len(str(num)) == 1:
                return int(num)
        return int(num)

# if running locally then uncomment below lines
# c1 = Solution()
# print(c1.addDigits(38))
