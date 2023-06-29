class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from itertools import combinations
        nums = sorted(nums)
        ans = 0
        combos = combinations(nums, 3)
        for combo in combos:
            if len(combo) == len(set(combo)):
                ans += 1
        return ans