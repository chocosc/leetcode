class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans_list = []
        ans = []
        for r in range(rows):
            for c in range(cols):
                ans_list.append([abs(rCenter-r) + abs(cCenter-c), [r, c]])
        ans_list = sorted(ans_list)
        for _, dot in ans_list:
            ans.append(dot)
        return ans

