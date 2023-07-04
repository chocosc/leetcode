class Solution:
    def minStartValue(self, nums: List[int]) -> int:
          
        nums_sum = []

        for i in range(len(nums)):
            nums_sum.append(sum(nums[:i+1]))

        if min(nums_sum) >= 1:
            return 1
        else:
            return abs(min(nums_sum))+1
