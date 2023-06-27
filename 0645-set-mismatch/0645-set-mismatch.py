class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        ans_list = []
        check_num = [x+1 for x in range(len(nums))]
        for key, value in counter.items():
            if value == 2:
                ans_list.append(key)
                break
        for num in check_num:
            if num not in counter:
                ans_list.append(num)
                break
        return ans_list
        
