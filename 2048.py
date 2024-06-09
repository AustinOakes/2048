import numpy as np

board = []


# Set the initial state of the board. In this case a 4x4 square.
def SetBoard(board):
    for i in range(0, 4):
        board.append([0] * 4)
    
    AddTile(board)

# Populate a new "tile" on the board
def AddTile(board):
    i = np.random.randint(4)
    j = np.random.randint(4)

    while board[i][j]:
        i = np.random.randint(4)
        j = np.random.randint(4)

    board[i][j] = 2

# Start by setting up the board
SetBoard(board)

'''
for i in range(1, 11):
    AddTile(board)
'''

# Print the current state of the board for testing purposes
# Currently set to print each list element (other lists) on a new line via * operatior and sep='\n'
print(*board, sep='\n')