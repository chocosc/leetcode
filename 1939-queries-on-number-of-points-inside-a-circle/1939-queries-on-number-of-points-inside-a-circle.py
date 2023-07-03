class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for [q_x, q_y, r] in queries:
            temp = 0
            for [x, y] in points:
                if r**2 >= ((q_x-x)**2 + (q_y-y)**2):
                    temp += 1
            ans.append(temp)
        return ans

