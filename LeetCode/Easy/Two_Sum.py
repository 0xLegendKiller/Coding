class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for j in range(0,len(nums)):
            for i in range(0,len(nums)):
                if i == j:
                    continue
                else:
                    if nums[j]==target-nums[i]:
                        
                        res.append(j)
                        res.append(i)
                        break
        
        res2 = []
        res2.append(res[0])
        res2.append(res[1])
        return res2            
