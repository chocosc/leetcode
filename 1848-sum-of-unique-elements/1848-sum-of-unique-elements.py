class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        ans = 0
        for key, value in counter.items():
            if value == 1:
                ans += key
        return ans