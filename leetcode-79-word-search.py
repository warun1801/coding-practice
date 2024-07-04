"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
""" 

def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    path = set()
    
    def backtrack(r, c, word_idx):
        if (r < 0 or c < 0) or\
            (r >= rows or c >= cols) or\
            ((r, c) in path) or\
            (word[word_idx] != board[r][c]):
                return False
            
        print(word[word_idx], r, c)
        if word_idx == len(word) - 1:
            return True
            
        path.add((r,c))
        
        ans = backtrack(r + 1, c, word_idx + 1) or\
                backtrack(r - 1, c, word_idx + 1) or\
                backtrack(r, c + 1, word_idx + 1) or\
                backtrack(r, c - 1, word_idx + 1)
        
        path.remove((r, c))
        
        return ans
        
    ans = False    
    for i in range(rows):
        for j in range(cols):
            ans = ans or backtrack(i, j, 0)
            
    return ans
        
        
if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    
    print(exist(board, word))
        
        
    