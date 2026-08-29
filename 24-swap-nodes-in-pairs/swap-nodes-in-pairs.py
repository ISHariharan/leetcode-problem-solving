# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        newnode = ListNode(-1)
        newnode.next = head

        ptr = newnode

        while ptr.next != None and ptr.next.next != None:
            first = ptr.next
            second = ptr.next.next

            # Swap the nodes
            first.next = second.next
            second.next = first
            ptr.next = second

            # Move to the next pair
            ptr = first

        return newnode.next