class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
        if divisor !=0:
            result = int(dividend / divisor)
        else:
            return None
            
        if -2**31 <= result <= 2**31 - 1:
            return (result)
        elif result>2**31-1:
            return (2**31-1)
        else:
            return (result)

