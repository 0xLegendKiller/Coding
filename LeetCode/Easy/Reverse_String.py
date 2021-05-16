class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        left = 0
        right = -1
        while left < s_len // 2:
            temp_left = s[left]
            s[left] = s[right]
            s[right] = temp_left
            left = left + 1
            right = right - 1
