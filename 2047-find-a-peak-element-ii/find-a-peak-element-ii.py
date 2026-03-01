class Solution:
    def refactorMatrix(self, mat : List[List[int]]):
        zeros_list = [-1]*(len(mat[0]) + 2)
        for row in mat:
            row.insert(0, -1)
            row.append(-1)
        mat.insert(0, zeros_list)
        mat.append(zeros_list)
        return mat
    def findPeakGrid(self, mat: List[List[int]]) -> List[List[int]]:
        row, column = 0, 0
        mat = self.refactorMatrix(mat);
        maxRow, maxColumn = len(mat), len(mat[0])
        result = []
        while(row < maxRow):
            element = mat[row][column]
            top = (row - 1 >= 0) and (element > mat[row - 1][column])
            right = (column + 1 < maxColumn) and (element > mat[row][column + 1])
            bottom = (row + 1 < maxRow) and (element > mat[row + 1][column])
            left = (column - 1 >= 0) and (element > mat[row][column - 1])
            if(top and right and bottom and left):
                result = [row - 1, column - 1]
            column += 1
            if(column == maxColumn):
                column = 0
                row += 1
        return result