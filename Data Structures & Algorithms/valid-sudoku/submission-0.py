class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        box = set()

        for i in range(9):
            for j in range(9):

                num = board[i][j]
                if num == ".":
                    continue

                row_key = (i, num)
                col_key = (j, num)
                box_key = (i // 3, j // 3, num)

                if row_key in rows or col_key in cols or box_key in box:
                    return False

                rows.add(row_key)
                cols.add(col_key)
                box.add(box_key)

            return True