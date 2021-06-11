class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                magazine = magazine.replace(char, '', 1)
        return True

# use only when ran locally
# s1 = Solution()
# print(s1.canConstruct("aab", "baa"))
