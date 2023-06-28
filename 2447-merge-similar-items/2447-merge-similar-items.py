class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        item_dict = defaultdict(int)
        ans_list = []
        for value, weight in items1:
            item_dict[value] += weight
        for value, weight in items2:
            item_dict[value] += weight
        for key, value in item_dict.items():
            ans_list.append([key, value])
        return sorted(ans_list)
