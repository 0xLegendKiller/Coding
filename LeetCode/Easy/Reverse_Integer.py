class Solution:
    def reverse(self, x: int) -> int:
        result = ''.join(list(str(abs(x)))[::-1])
        
        if x < 0: 
            result = '-' + result
        
        result = int(result)
        
        if result <= pow(-2,31) or result >= pow(2,31)-1: 
            return 0
        
        return result
