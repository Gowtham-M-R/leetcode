class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        c=len(matrix)
        for i in range(c):
            for j in range(i,c):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix