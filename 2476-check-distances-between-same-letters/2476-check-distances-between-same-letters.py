class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        from collections import defaultdict
        s_dict = defaultdict(list)
        s_list = []
        for i in range(len(s)):
            s_dict[s[i]].append(i)
        for key, value in s_dict.items():
            if distance[ord(key)-97] != value[1] - (value[0] + 1):
                return False
        return True