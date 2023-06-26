class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        ans_list = []
        for key, value in counter.items():
            if value >= 2:
                ans_list.append(key)
        return ans_list