import numpy as np
import pynput.keyboard as kb

board = []

# Set the initial state of the board. In this case a 4x4 square.
def SetBoard(board):
    for _ in range(0, 4):
        board.append([0] * 4)


# Check adjacent tiles for any possible moves
def IsMoreMoves(board):

    for i in range(len(board)):
        for j in range(len(board[i])):
            # Check if the current cell is empty
            if board[i][j] == 0:
                return True
            # Check the cell to the right if it's not the last column
            if j < len(board[i]) - 1 and board[i][j] == board[i][j + 1]:
                return True
            # Check the cell below if it's not the last row
            if i < len(board) - 1 and board[i][j] == board[i + 1][j]:
                return True
    return False

# Populate a new "tile" on the board
def AddTile(board, num=0):
    
    if not any(0 in row for row in board):
        return

    i = np.random.randint(4)
    j = np.random.randint(4)

    while board[i][j] != 0 and IsMoreMoves(board):
        i = np.random.randint(4)
        j = np.random.randint(4)

    if num == 0:
        board[i][j] = np.random.choice([2, 4])
        print("Added tile")
    else:
        board[i][j] = num

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

def MoveTiles(board, dir):

    merged = []

    for i in range(0, 4):
        merged.append([False] * 4)

    match dir:
        case 'U':
            for i in range(1, 4):
                for j in range(0, 4): 
                        
                    temp = i

                    # Move upwards in the column until we find an empty spot
                    while temp > 0 and board[temp-1][j] == 0:
                        board[temp-1][j] = board[temp][j]
                        board[temp][j] = 0
                        temp -= 1

                    # Merge the tiles if they are the same and the top one hasn't been merged already
                    if temp > 0 and board[temp-1][j] == board[temp][j] and not merged[temp-1][j]:
                        board[temp-1][j] *= 2
                        board[temp][j] = 0
                        merged[temp-1][j] = True

        case 'D':
            for i in range(3, -1, -1):
                for j in range(4): 
                        
                    temp = i

                    # Move downwards in the column until we find an empty spot
                    while temp < 3 and board[temp+1][j] == 0:
                        board[temp+1][j] = board[temp][j]
                        board[temp][j] = 0
                        temp += 1

                    # Merge the tiles if they are the same and the top one hasn't been merged already
                    if temp < 3 and board[temp+1][j] == board[temp][j] and not merged[temp+1][j]:
                        board[temp+1][j] *= 2
                        board[temp][j] = 0
                        merged[temp+1][j] = True

        case 'L':
            for j in range(1, 4):
                for i in range(0, 4): 
                        
                    temp = j

                    # Move left in the row until we find an empty spot
                    while temp > 0 and board[i][temp-1] == 0:
                        board[i][temp-1] = board[i][temp]
                        board[i][temp] = 0
                        temp -= 1

                    # Merge the tiles if they are the same and the top one hasn't been merged already
                    if temp > 0 and board[i][temp-1] == board[i][temp] and not merged[i][temp-1]:
                        board[i][temp-1] *= 2
                        board[i][temp] = 0
                        merged[i][temp-1] = True

        case 'R':
            for j in range(3, -1, -1):
                for i in range(4): 
                        
                    temp = j

                    # Move right in the row until we find an empty spot
                    while temp < 3 and board[i][temp+1] == 0:
                        board[i][temp+1] = board[i][temp]
                        board[i][temp] = 0
                        temp += 1

                    # Merge the tiles if they are the same and the top one hasn't been merged already
                    if temp < 3 and board[i][temp+1] == board[i][temp] and not merged[i][temp+1]:
                        board[i][temp+1] *= 2
                        board[i][temp] = 0
                        merged[i][temp+1] = True

        case _:
            print("User did not press an arrow key")

# Prompt the user for to press an arrow key
def PromptUser(board):
    print("Press an arrow key!:")

    # Closure function to allow us to pass board to the MoveTiles function
    def on_press(key):
        if key == kb.Key.up:
            MoveTiles(board, 'U')
            return False
        elif key == kb.Key.down:
            MoveTiles(board, 'D')
            return False
        elif key == kb.Key.left:
            MoveTiles(board, 'L')
            return False
        elif key == kb.Key.right:
            MoveTiles(board, 'R')
            return False

    with kb.Listener(on_press=on_press) as listener:
        listener.join()

def IsFinished(board):
    
    # Size of tile needed to win the game
    WINNING_SCORE = 2048

    # Check if any of the lists within board contain the winning score
    if any(WINNING_SCORE in row for row in board):
        print("YOU WON!!!")
        return True
    else:
        return False

#****************Testing section******************#

# Start by setting up the board, and starting of the first turn
SetBoard(board)

# Continue while the game is not completed

while not IsFinished(board) and IsMoreMoves(board):
    AddTile(board)
    PrintBoard(board)
    PromptUser(board)
    
print("game over")
