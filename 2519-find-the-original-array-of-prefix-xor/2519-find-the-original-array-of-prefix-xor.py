class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref

        ans_list = []
        ans_list.append(pref[0])

        for i in range(1, len(pref)):
            ans_list.append(pref[i] ^ pref[i-1])

        return ans_list