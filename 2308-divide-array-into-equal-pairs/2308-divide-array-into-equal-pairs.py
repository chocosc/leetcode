class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for value in c.values():
            if value % 2 != 0:
                return False
        return True