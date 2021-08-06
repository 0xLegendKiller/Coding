class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) != 0:
            if needle in haystack:
                pos = haystack.index(needle)
                return pos
            else:
                return -1                
        else:
            return 0
