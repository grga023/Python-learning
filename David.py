

print("Welcome let's play some battleships!")

board = []
wrong = []

for i in range(0,7):
    wrong.append([chr(0x274C)]*7)

for i in range(0,7):
    board.append([chr(0x1F7E9)]*7)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)

#%% Pravljenje i upis u file brodovi
import csv


cnt = 0
ships = 0

shipRow = [8]
shipCol = [8]

x = []
y = []
size = []
orientation = []

with open('brodovi.txt','r') as brodici:
    reader = csv.reader(brodici)
    for row in reader:
        x.append(row[0])
        y.append(row[1])
        size.append(row[2])
        orientation.append(row[3])
        cnt += 1   

prepare = []
for i in range(cnt):
    x[i] = x[i].replace('(','') 
    orientation[i] = orientation[i].replace(')','')   
    if orientation[i] == "v":
        tmp = i
        m = size[i]
        for o in range(int(m)):
            wrong[i][tmp] = chr(0x2693)
            tmp += 1
            ships += 1
    if orientation[i] == "h":
        tmp = i
        m = size[i]
        for o in range(int(m)):
            wrong[tmp][i] = chr(0x2693)
            tmp += 1
            ships += 1


Try = 0
correct = 0
while Try < 20:
    getTry = input("Insert cordinates:")
    getTry = getTry.replace('(', '').replace(')', '').replace(',', ' ')
    try:
        guess_col, guess_row = [int(x) for x in getTry.split()]

        guess_col -=1
        guess_row -=1

        if guess_row > 7 or guess_col > 7:
            print("Out of range max coll 7 and row 8")
        else:
            for obj in wrong:
                if board[guess_row][guess_col] == chr(0x274C) or board[guess_row][guess_col] == chr(0x2693):
                    print("You've guessed that one already")
                    break
                elif wrong[guess_row][guess_col] == chr(0x2693):
                    print("nice")
                    correct += 1
                    board[guess_row][guess_col] = chr(0x2693)
                    print_board(board)
                    if correct == ships:
                        Try = 20
                        print("Congratulation!")
                    break
                elif wrong[guess_row][guess_col] == chr(0x274C):
                    print(":(")
                    board[guess_row][guess_col] = chr(0x274C)
                    print_board(board)
                    Try += 1
                    if Try == 20:
                        print("Better luck next time")
                    break

    except:
        print("Wrong number format") 

    
print("End")
print_board(board)
