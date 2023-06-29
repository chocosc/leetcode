class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_check = [0, 3, 6]
        line_check = [x for x in range(9)]
        
        from collections import Counter

        for i in square_check:
            for j in square_check:
                temp = ''
                temp += board[i][j]
                temp += board[i][j+1]
                temp += board[i][j+2]
                temp += board[i+1][j]
                temp += board[i+1][j+1]
                temp += board[i+1][j+2]
                temp += board[i+2][j]
                temp += board[i+2][j+1]
                temp += board[i+2][j+2]
                c = Counter(temp)
                del c['.']
                for value in c.values():
                    if value > 1:
                        return False
        
        for k in line_check:
            temp = ''
            temp += board[k][0]
            temp += board[k][1]
            temp += board[k][2]
            temp += board[k][3]
            temp += board[k][4]
            temp += board[k][5]
            temp += board[k][6]
            temp += board[k][7]
            temp += board[k][8]
            c = Counter(temp)
            del c['.']
            for value in c.values():
                if value > 1:
                    return False
        
        for l in line_check:
            temp = ''
            temp += board[0][l]
            temp += board[1][l]
            temp += board[2][l]
            temp += board[3][l]
            temp += board[4][l]
            temp += board[5][l]
            temp += board[6][l]
            temp += board[7][l]
            temp += board[8][l]
            c = Counter(temp)
            del c['.']
            for value in c.values():
                if value > 1:
                    return False
        
        return True
        