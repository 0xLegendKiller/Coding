class Solution:
    def letterCombinations(self, digits: str):
        sets = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        lister = []
        if len(digits) == 1:
            val1 = sets[digits[0]]
            for i in range(len(val1)):
                lister.append(val1[i])
            return lister
        elif len(digits) == 2:
            val1 = sets[digits[0]]
            val2 = sets[digits[1]]
            for i in range(len(val1)):
                for j in range(len(val2)):
                    lister.append(val1[i] + val2[j])
            return lister
        elif len(digits) == 3:
            val1 = sets[digits[0]]
            val2 = sets[digits[1]]
            val3 = sets[digits[2]]
            for i in range(len(val1)):
                for j in range(len(val2)):
                    for k in range(len(val3)):
                        lister.append(val1[i] + val2[j] + val3[k])

            return lister
        elif len(digits) == 4:
            val1 = sets[digits[0]]
            val2 = sets[digits[1]]
            val3 = sets[digits[2]]
            val4 = sets[digits[3]]
            for i in range(len(val1)):
                for j in range(len(val2)):
                    for k in range(len(val3)):
                        for l in range(len(val4)):
                            lister.append(val1[i] + val2[j] + val3[k] + val4[l])
            return lister
        else:
            return lister


# digits = str(input())
# s1 = Solution()
# print(s1.letterCombinations(digits=digits))
# Runtime: 24 ms, faster than 95.77% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14 MB, less than 96.22% of Python3 online submissions for Letter Combinations of a Phone Number.
