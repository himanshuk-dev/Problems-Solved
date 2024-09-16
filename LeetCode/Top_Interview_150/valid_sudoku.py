# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------


# Valid Sudoku
# Medium
# Topics
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# Initialize data structures:

# Create a list of 9 sets for rows.
# Create a list of 9 sets for columns.
# Create a list of 9 sets for 3x3 sub-boxes.
# Loop through each cell in the Sudoku board:

# For each row i (from 0 to 8):
# For each column j (from 0 to 8):

# Calculate the box index:
# Compute box_index = (i // 3) * 3 + (j // 3) to identify which 3x3 box the current cell belongs to.
# Check if the cell is empty:
# If the cell contains a '.', move to the next cell.
# Check for duplicates:
# If the current number is already in the corresponding row, column, or box set:
# Return False (the board is invalid).
# Update sets:
# Add the current number to the corresponding row, column, and box sets.
# Return true if no duplicates found:

# If the loop completes without returning False, return True (the board is valid).


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                
                box_index = (i // 3) * 3 + (j // 3)
                num = board[i][j]

                if num == '.':
                    continue
                
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        return True
                