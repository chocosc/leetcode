class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i in range(len(startTime)):
            if queryTime in [x for x in range(startTime[i], endTime[i]+1)]:
                ans += 1
        return ans