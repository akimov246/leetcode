from copy import deepcopy

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        board_letters = set([board[i][j] for i in range(len(board))
                                         for j in range(len(board[0]))])
        word_letters = set(word)
        if not word_letters.issubset(board_letters):
            return False
        if not word:
            return True
        first_letter = word[0]
        first_letter_indexes = {(i, j) for i in range(len(board))
                                       for j in range(len(board[i])) if board[i][j] == first_letter}

        for r, c in first_letter_indexes:
            board_tmp = deepcopy(board)
            board_tmp[r][c] = '0'
            if self.search(board_tmp, word[1:], r, c):
                return True
        return False

    def search(self, board: list[list[str]], word: str, row_idx: int, column_idx: int):
        if not word:
            return True

        target_letter = word[0]

        up = (row_idx - 1 if row_idx - 1 >= 0 else len(board), column_idx)
        right = (row_idx, column_idx + 1 if column_idx + 1 < len(board[row_idx]) else len(board[row_idx]))
        down = (row_idx + 1 if row_idx + 1 < len(board) else len(board), column_idx)
        left = (row_idx, column_idx - 1 if column_idx - 1 >= 0 else len(board[row_idx]))

        directions = []
        for r, c in [up, right, down, left]:
            try:
                if board[r][c] == target_letter:
                    board_tmp = deepcopy(board)
                    board_tmp[r][c] = '0'
                    directions.append((board_tmp, word[1:], r, c))
            except: ...

        if not directions:
            return False

        return any(self.search(*d) for d in directions)




print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
