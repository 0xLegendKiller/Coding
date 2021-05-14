class Solution:
    def hammingWeight(self, n: int) -> int:
        l = str(n)
        l1 = bin(int(l))
        count  = 0
        for ele in l1[2:]:
            if ele == "1":
                count = count + 1
            else:
                continue
        return (count)
