class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        columns=[set() for _ in range(9)]
        grids=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]
                grid= (i//3)*3+(j//3)
                if num=='.':
                    continue
                if num in rows[i] or num in columns[j] or num in grids[grid] :
                    return False
                else:
                    rows[i].add(num)
                    columns[j].add(num)
                    grids[grid].add(num)
        return True
