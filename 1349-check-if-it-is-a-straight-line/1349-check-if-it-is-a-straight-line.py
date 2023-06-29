class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] - coordinates[0][0] == 0:
            x = coordinates[0][0]
            for dot in coordinates:
                if dot[0] != x:
                    return False
            return True
        else:
            n = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            a = coordinates[0][1] - (n * coordinates[0][0])
            for dot in coordinates:
                if (n * dot[0]) + a != dot[1]:
                    return False
            return True