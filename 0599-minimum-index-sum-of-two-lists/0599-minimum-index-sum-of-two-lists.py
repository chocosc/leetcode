class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        from collections import Counter, defaultdict
        both_list = []
        ans_dict = defaultdict(list)
        counter = Counter(list1 + list2)
        for key, value in counter.items():
            if value == 2:
                both_list.append(key)
        for word in both_list:
            ans_dict[list1.index(word)+list2.index(word)].append(word)
        return ans_dict[min(ans_dict)]