class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = []
        odd = []
        for num in position:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        return min(len(even), len(odd))

        