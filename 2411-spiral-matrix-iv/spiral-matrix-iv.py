# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        matrix = [[-1] * n for _ in range(m)]
        # return matrix
        while (top <= bottom and left <= right):
            for index in range(left, right+1):
                if index < right+1 and head != None :
                    matrix[top][index]= head.val
                    head = head.next
                    if(head == None):
                        break
            top += 1
            
            if top <= bottom :
                for index in range(top, bottom+1):
                    if index < bottom+1 and head != None:
                        matrix[index][right] = head.val
                        head = head.next
            right -= 1

            if left <= right and top <= bottom: 
                for index in range(right, -1, -1):
                    if index >= left and head != None:
                        matrix[bottom][index] = head.val
                        head = head.next
            bottom -= 1

            if left <= right and top <= bottom: 
                for index in range(bottom, -1, -1):
                    if index >= top and head != None:
                        matrix[index][left] = head.val
                        head = head.next
                left += 1
        return matrix