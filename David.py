
import csv
print("Welcome let's play some battleships!")

board = []
wrong = []
#ovde ti se kreiraju dve table 7*7 jedna sa zelenim jedna 
# sa prodicima i iksicima
for i in range(0,7):
    wrong.append([chr(0x274C)]*7)

for i in range(0,7):
    board.append([chr(0x1F7E9)]*7)

def print_board(board):
    for row in board:
        print (" ".join(row))

#printasa tablu ne znam da lis te koristili fje ali ti je mnogooo lakse sa njima
# i iskreno ne predlazem ti da ih sklanjas prevelik je seks bez njih
print_board(board)

#%% Pravljenje i upis u file brodovi
cnt = 0
ships = 0

shipRow = [8]
shipCol = [8]

x = []
y = []
size = []
orientation = []

#koristi cvs i reci mu ako te nesto pita da si nasao na netu
#i da ti je bilo lakse tako da ga koristis

with open('brodovi.txt','r') as brodici:
    reader = csv.reader(brodici)
    for row in reader:
        x.append(row[0])
        y.append(row[1])
        size.append(row[2])
        orientation.append(row[3])
        cnt += 1   

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
    #ovaj try exception blok ti je ovde da spreci pogresan unos 
    # tipa kada se unosi da se ne unese slucajno 22 ili tako neki broj
    #  mada sobzirom da ce te vi koristiti (5,6) format mozes ga obrisati.
    #  ja sam ga stavio pa sad ako ste ga spominjali ikad ne diraj ga bolje
    #  msm sprecava da ti program pukne. al ono kako god
    try:
        #ovo ti odvaja dva broja
        guess_col, guess_row = [int(x) for x in getTry.split()]

        guess_col -=1
        guess_row -=1

        if guess_row > 7 or guess_col > 7:
            print("Out of range max coll 7 and row 7")
        else:
            #ovde prolazis kroz sve clanove svaki put i proverava se da li 
            # su sidra ili iksici ako je izabran x ili sidro nista se ne desava
            # ako je brodic selektuje se i to je to
            # a ako je x izabran koji nije pre izabran onda se Try cnt povecava i ako lupi 20 program se zavrsava 
            #kontam da ces skontati al ako ne skontas mozemo se cuti tako da ono
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

    print_board(board)
print("End")

