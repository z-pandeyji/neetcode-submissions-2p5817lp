class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = []
        for _ in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                box_id = (r // 3) * 3 + (c // 3)
                if val in boxes[box_id]:
                    return False
                boxes[box_id].add(val)
        return True
        