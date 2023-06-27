class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        index_list = [x for x in range(len(nums))]
        cur_max = 1
        cur_len = 1
        for i in index_list[:-1]:
            if nums[i+1] > nums[i]:
                cur_len += 1
                if cur_len > cur_max:
                    cur_max = cur_len
            elif nums[i+1] == nums[i]:
                cur_len = 1
            else:
                cur_len = 1
        return cur_max