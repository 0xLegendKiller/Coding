# URL :- `https://leetcode.com/problems/valid-palindrome/`
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(ch for ch in s if ch.isalnum())
        print(s2)
        return (s2.lower() == s2[::-1].lower())
     
 
