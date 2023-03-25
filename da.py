#%%
from random import randint, random


board = []

for i in range(0,5):
    board.append(["0"]*5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print("Let's play Battleship")
print_board(board)

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board[0])-1)


ship_row = random_row(board)
ship_col = random_col(board)


# print(ship_col)
# print(ship_row)
for turn in range(10):
    print("Turn", turn+1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratualtions! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Opps, that's not even in the ocean")
        elif board[guess_row][guess_col] == "X":
            print("You've guessed that one already")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col]= "X"
            if turn == 9:
                print("Game Over")
            
        print_board(board)


input("Press Enter to Exit;")
# %%
