class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        if row == 1:
            return matrix[0]   
        arr = []
        if col == 1:
            for mat in matrix:
                arr.append(mat[0])
            return arr
        top = 0
        left = 0
        right = col - 1
        bottom = row - 1

        while (top <= bottom and left <= right):
            for index in range(left, right+1):
                if index < right+1 :
                    arr.append(matrix[top][index])
            top += 1
            
            if top <= bottom :
                for index in range(top, bottom+1):
                    if index < bottom+1:
                        arr.append(matrix[index][right])
            right -= 1

            if left <= right and top <= bottom: 
                for index in range(right, -1, -1):
                    if index >= left:
                        arr.append(matrix[bottom][index])
            bottom -= 1

            if left <= right and top <= bottom: 
                for index in range(bottom, -1, -1):
                    if index >= top:
                        arr.append(matrix[index][left])
                left += 1
        return arr
            