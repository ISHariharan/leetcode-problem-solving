class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattenArr = []
        for row in mat:
            for item in row:
                flattenArr.append(item)
        length = len(flattenArr)
        if r * c > length or r * c < length:
            return mat
        index = 0
        mat = [[0] * c for index in range(r)]
        for row in range(r):
            for col in range(c):
                mat[row][col] = flattenArr[index]
                index += 1
        return mat