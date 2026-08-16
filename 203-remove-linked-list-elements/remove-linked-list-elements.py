# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, pointer = head, head
        while pointer != None:
            if pointer.val == val:
                prev.next = pointer.next
                pointer = pointer.next
            else:
                prev = pointer
                pointer = pointer.next
        if head != None and head.val == val:
            return head.next
        return head