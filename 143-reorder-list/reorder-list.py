# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        original = []
        temp = head
        while temp != None:
            original.append(temp.val)
            temp = temp.next
        ptr = None
        first = 0
        left = 0
        right = len(original) - 1
        reordered = []
        while left <= right : 
            if left == right:
                reordered.append(original[left])
            else:
                reordered.append(original[left])
                reordered.append(original[right])
            left += 1
            right -= 1
        temp = head
        for ele in reordered:
            temp.val = ele
            temp = temp.next

        return head