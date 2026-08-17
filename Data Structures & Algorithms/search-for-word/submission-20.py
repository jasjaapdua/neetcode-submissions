from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, pos):
            if r >= rows or c >= cols or r < 0 or c < 0:
                return False

            if (r, c) in path:
                return False

            if board[r][c] != word[pos]:
                return False

            if pos == len(word) - 1:
                return True

            path.add((r, c))

            found = (
                dfs(r - 1, c, pos + 1) or
                dfs(r + 1, c, pos + 1) or
                dfs(r, c - 1, pos + 1) or
                dfs(r, c + 1, pos + 1)
            )

            path.remove((r, c))

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False