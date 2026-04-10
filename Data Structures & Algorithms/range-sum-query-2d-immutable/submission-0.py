class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.ps = [[0 for _ in range(cols + 1)] for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                self.ps[r+1][c+1] = (
                    matrix[r][c] +  # current cell
                    self.ps[r][c+1] +  # above 
                    self.ps[r+1][c]  # left
                    - self.ps[r][c]) # overlap

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Using the formula : 
        # A: bottom - right total, B: above rectange, C: left rectange, D: overlap added twice

        A = self.ps[row2 + 1][col2 + 1]
        B = self.ps[row1][col2 + 1]
        C = self.ps[row2 + 1][col1]
        D = self.ps[row1][col1]

        return A - B - C + D


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)