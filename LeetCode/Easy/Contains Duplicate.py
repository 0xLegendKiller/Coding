# Solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!= len(nums)

arr = [1,2,3,1]
c1 = Solution()
print(c1.containsDuplicate(arr))
        
# Solution 2 -- Exceeds the time limit
class Solution2:
    def containsDuplicate(self, nums):
        lst = []
        for i in nums:
            if i in lst:
                return True
            else:
                lst.append(i)
        return False

arr = [1,2,3,1]
c1 = Solution2()
print(c1.containsDuplicate(arr))
