'''
Title - 36. Valid Sudoku
Link - https://leetcode.com/problems/valid-sudoku/
'''

class Solution:

    def checkSet(self, cell: str, visited: set):
        if cell!="." and cell in visited:
            return False
        else:
            visited.add(cell)
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows and cols
        for i in range(0,9):
            row_visited = set()
            col_visited = set()
            for j in range(0,9):
                if not self.checkSet(board[i][j], row_visited):
                    return False
                if not self.checkSet(board[j][i], col_visited):
                    return False
        
        # check grid
        for gridi in range(0,9,3):
            for gridj in range(0,9,3):
                grid_visited = set()
                for a in range(0,3):
                    for b in range(0,3):
                        i,j = gridi+a, gridj+b
                        if not self.checkSet(board[i][j], grid_visited):
                            return False
        
        return True
