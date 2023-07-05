class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        num_dict = defaultdict(list)
        ans_list = []

        for i, num in enumerate(groupSizes):
            num_dict[num].append(i)

        for k in num_dict:
            for j in range(len(num_dict[k])//k):
                ans_list.append(num_dict[k][j*k:j*k+k])
        
        return ans_list