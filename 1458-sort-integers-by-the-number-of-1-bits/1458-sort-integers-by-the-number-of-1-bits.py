class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp_list = []
        ans_list = []
        for num in arr:
            temp_list.append([bin(num)[2:].count('1'), num])
        for _, value in sorted(temp_list):
            ans_list.append(value)
        return ans_list