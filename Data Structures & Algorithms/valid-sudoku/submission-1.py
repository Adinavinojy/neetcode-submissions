class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[] for _ in range(9)]
        columns=[[] for _ in range(9)]
        grids=[[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]
                grid= (i//3)*3+(j//3)
                if num=='.':
                    continue
                if num in rows[i] or num in columns[j] or num in grids[grid] :
                    return False
                else:
                    rows[i].append(num)
                    columns[j].append(num)
                    grids[grid].append(num)
        return True
