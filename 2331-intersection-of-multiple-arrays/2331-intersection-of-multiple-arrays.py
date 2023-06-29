class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = Counter(nums[0])
        for num in nums:
            res &= Counter(num)
        return sorted(res.elements())