class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        
        ans_list = []
        for i in range(len(words)):
            if words[i] == target:
                ans_list.append(abs(startIndex-i))
                ans_list.append(abs(abs(startIndex-i)-len(words)))
        
        return min(ans_list)

        