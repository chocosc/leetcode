# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node_l1 = l1
        cur_node_l2 = l2
        l1_str = ''
        l2_str = ''

        while cur_node_l1:
            l1_str += str(cur_node_l1.val)
            cur_node_l1 = cur_node_l1.next
        
        while cur_node_l2:
            l2_str += str(cur_node_l2.val)
            cur_node_l2 = cur_node_l2.next
        
        ans_list = []
        ans_node = ListNode()
        cur_node = ans_node

        for num in str(int(l1_str[::-1]) + int(l2_str[::-1]))[::-1]:
            ans_list.append(int(num))

        for i in range(len(ans_list)):
            cur_node.val = ans_list[i]
            if i == len(ans_list)-1:
                break
            cur_node.next = ListNode(0)
            cur_node = cur_node.next

        return ans_node

        
        
        