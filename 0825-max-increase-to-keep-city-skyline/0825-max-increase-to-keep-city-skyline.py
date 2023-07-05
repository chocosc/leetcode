class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = []
        col_max = []
        ans = 0

        for x in range(len(grid)):
            temp = []
            row_max.append(max(grid[x]))
            for y in range(len(grid[0])):
                temp.append(grid[y][x])
            col_max.append(max(temp))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += max(grid[i][j], min(col_max[j], row_max[i])) - grid[i][j]

        return ans