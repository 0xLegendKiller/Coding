class Solution:
    def romanToInt(self, s: str) -> int:
        change = {
            'I': '1',
            'V': '5',
            'X': '10',
            'L': '50',
            'C': '100',
            'D': '500',
            'M': '1000'
        }
        sum = 0
        #print(s)
        for i in range(len(s)):
            if i < len(s)-1:
                if int(change.get(s[i]))>=int(change.get(s[i+1])):
                    sum = sum + int(change.get(s[i]))
                else:
                    sum = sum - int(change.get(s[i]))
            else:
                sum = sum + int(change.get(s[i]))

        return sum
