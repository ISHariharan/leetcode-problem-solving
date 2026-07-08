class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        matrix = [[0] * n for _ in range(n)]
        count = 1
        # return matrix
        while (top <= bottom and left <= right):
            for index in range(left, right+1):
                if index < right+1 :
                    matrix[top][index]= count
                    count += 1
            top += 1
            
            if top <= bottom :
                for index in range(top, bottom+1):
                    if index < bottom+1:
                        matrix[index][right] = count
                        count += 1
            right -= 1

            if left <= right and top <= bottom: 
                for index in range(right, -1, -1):
                    if index >= left:
                        matrix[bottom][index] = count
                        count += 1
            bottom -= 1

            if left <= right and top <= bottom: 
                for index in range(bottom, -1, -1):
                    if index >= top:
                        matrix[index][left] = count
                        count += 1
                left += 1
        return matrix