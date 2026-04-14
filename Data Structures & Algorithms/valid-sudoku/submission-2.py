class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                box = (r//3, c//3)
                if num in rows[r] or num in cols[c] or num in boxes.get(box, set()):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                if box not in boxes:
                    boxes[box] = set()
                boxes[box].add(num)
        return True