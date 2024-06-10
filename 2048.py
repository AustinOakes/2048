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
                    PrintBoard(board)
                        
        case 'D':
            for i in range(2, -1, -1):
                for j in range(4): 
                        
                    temp = i

                    # Move upwards in the column until we find an empty spot
                    while temp < 3 and board[temp+1][j] == 0:
                        board[temp+1][j] = board[temp][j]
                        board[temp][j] = 0
                        temp += 1

                    # Merge the tiles if they are the same and the top one hasn't been merged already
                    if temp < 3 and board[temp+1][j] == board[temp][j] and not merged[temp+1][j]:
                        board[temp+1][j] *= 2
                        board[temp][j] = 0
                        merged[temp+1][j] = True
                    PrintBoard(board)
        case 'L':
            for j in range(1, 4):
                for i in range(0, 4): 
                        
                    temp = j

                    # Move left in the row until we find an empty spot
                    while temp > 0 and board[i][temp-1] == 0:
                        board[i][temp-1] = board[i][temp-1]
                        board[i][temp] = 0
                        temp -= 1

                    # Merge the tiles if they are the same and the top one hasn't been merged already
                    if temp > 0 and board[i][temp-1] == board[i][temp] and not merged[i][temp-1]:
                        board[i][temp-1] *= 2
                        board[i][temp] = 0
                        merged[i][temp-1] = True
                    PrintBoard(board)
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

for i in range (0, 10):
    AddTile(board)

print("Start:")
PrintBoard(board)

PromptUser(board)
#PrintBoard(board)



    
 