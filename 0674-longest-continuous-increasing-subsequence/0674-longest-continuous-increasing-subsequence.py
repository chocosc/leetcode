class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur_max = 1
        cur_len = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur_len += 1
                if cur_len > cur_max:
                    cur_max = cur_len
            else:
                cur_len = 1
        return cur_max