class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans_list = []
        ans = 0
        for box, units in boxTypes:
            ans_list.append([units, box])
        ans_list = sorted(ans_list, reverse=True)
        for units, box in ans_list:
            if box <= truckSize:
                ans += units * box
                truckSize -= box
            else:
                ans += units * truckSize
                break
        return ans
            