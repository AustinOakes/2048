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

    board[i][j] = np.random.choice([2, 4])

# Print the current state of the board
def PrintBoard(board):

    # For each tile inside each board list...
    for list in board:
        for tile in list:
            # Print out the number of leading characters 
            leadChars = 4 - len(str(tile))
            print( "[" + ("*" * leadChars) + str(tile) + "] ", end="")

        print("\n", end="")   

    print()

# Start by setting up the board
SetBoard(board)

#****************Testing section******************#

PrintBoard(board)


 