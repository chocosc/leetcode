class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        ans_list = []
        for r in range(len(nums)+1):
            for combo in combinations(nums, r):
                combo = sorted(combo)
                if combo in ans_list:
                    continue
                ans_list.append(combo)
        return ans_list
