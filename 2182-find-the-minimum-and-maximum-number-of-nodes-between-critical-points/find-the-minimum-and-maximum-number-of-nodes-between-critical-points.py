# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head == None or head.next == None or head.next.next == None:
            return [-1, -1]
        # temp = head
        # arr = []
        left = head
        mid = head.next
        right = head.next.next
        index = 1
        indexes = []
        while right != None:
            if left.val < mid.val and right.val < mid.val:
                indexes.append(index)
            elif left.val > mid.val and right.val > mid.val:
                indexes.append(index)
            left = left.next
            mid = mid.next
            right = right.next
            index += 1
        # left = 0
        # right = 2
        # while right < len(arr):
        #     mid = (left + right) // 2
        #     if arr[left] < arr[mid] and arr[right] < arr[mid]:
        #         indexes.append(mid)
        #     elif arr[left] > arr[mid] and arr[right] > arr[mid]:
        #         indexes.append(mid)
        #     left += 1
        #     right += 1
        if indexes == [] or len(indexes) == 1:
            return [-1, -1]
        indexes = sorted(indexes)
        maxDistance = indexes[len(indexes) - 1] - indexes[0]
        minDistance = float('inf')
        left = 0
        right = 1
        while right < len(indexes):
            minDistance = min(abs(indexes[right] - indexes[left]) , minDistance)
            left += 1
            right += 1
        return [minDistance, maxDistance]
        # return indexes