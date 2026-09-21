class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            #rows
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        print(board[i][j])
                        return False
                    else:
                        seen.add(board[i][j])
        print("r good")
        for i in range(9):
            #cols
            seen = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        print(board[j][i])

                        return False
                    else:
                        seen.add(board[j][i])
        print("c good")

        for s in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (s // 3) * 3 + i
                    col = (s % 3) * 3 + j

                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            print(board[row][col])

                            return False
                        else:
                            seen.add(board[row][col])

                            

        return True