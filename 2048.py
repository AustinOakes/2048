import numpy as np
import pynput.keyboard as kb

board = []

# Set the initial state of the board. In this case a 4x4 square.
def SetBoard(board):
    for i in range(0, 4):
        board.append([0] * 4)
    
    AddTile(board, 2)

# Populate a new "tile" on the board
def AddTile(board, num=0):
    i = np.random.randint(4)
    j = np.random.randint(4)

    while board[i][j]:
        i = np.random.randint(4)
        j = np.random.randint(4)

    if num == 0:
        board[i][j] = np.random.choice([2, 4])
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

    match dir:
        case 'U':
            print("User pressed up!")
        case 'D':
            print("User pressed down!")
        case 'L':
            print("User pressed left!")
        case 'R':
            print("User pressed right!")
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



# Start by setting up the board
SetBoard(board)

#****************Testing section******************#

#PrintBoard(board)
PromptUser(board)



    
 