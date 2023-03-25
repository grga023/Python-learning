#%% Pocetna matrica sa zelenim kvadraticima

m = [chr(0x1F7E9) *7 for i in range(7)]

for i in m:
    for j in i:
        print(j, end=" ")
    print()  

#%% Pravljenje i upis u file brodovi
           
n = [chr(0x274C) *7 for i in range(7)]


for i in n:
    for j in i:
        print(j, end=" ")
    print()  






#%% Pravljenje matrice u koju se unose brodovi sa crvenim x
import csv
sidro = [chr(0x2693) *7 for i in range(7)]
file = open('brodovi.txt', 'w')

file.write('(0,0,2,v)\n(2,0,5,h)\n(0,6,3,h)\n(2,2,2,h)\n(5,2,4,v)')

file.close()
cnt = 0
# xMax, yMax = 7
x ,y, size, orientation= [],[],[],[]
with open('brodovi.txt','r') as f:
    reader = csv.reader(f)
    for row in reader:
        x.append(row[0])
        y.append(row[1])
        size.append(row[2])
        orientation.append(row[3])
        cnt += 1


print(cnt)        

for i in range(5):
    x[i] = x[i].replace('(','') 
    orientation[i] = orientation[i].replace(')','') 
    print(x[i], y[i], size[i], orientation[i])

unos = input("unesi korsinate")
print(unos)



# brodovi = []
# with open('brodovi.txt', 'r') as file:
#     for line in file:
#         x, y, size, orientation = line.strip().strip('()').split(',')
#         brodovi.append((int(x), int(y), int(size), orientation))
#         if orientation == 'h':
#             n[y] = n[y][:x] + chr(0x2693) + n[y][x+size:]
#         elif orientation == 'v':
#              n[x] = n[x][:y] + chr(0x2693) + n[x][y+size:]


# file = open('brodovi.txt', 'w')

# file.write('(0,0,2,v)\n(2,0,5,h)\n(0,6,3,h)\n(2,2,2,h)\n(5,2,4,v)')

# file.close()

# n = [['' for j in range(7)] for i in range(7)]


# with open('brodovi.txt', 'r') as file:
#     for line in file:
#         x, y, size, orientation = line.strip().strip('()').split(',')
#         x, y, size = int(x), int(y), int(size)

#         if orientation == 'h':
#             for j in range(size):
#                 n[x][y+j] = 'X'
#         elif orientation == 'v':
#             for i in range(size):
#                 n[x+i][y] = 'X'



# %%

# Kreirajte praznu matricu dimenzije 7x7
matrica = [[0 for j in range(7)] for i in range(7)]

# Otvorite fajl i pročitajte vrednosti
with open('brodovi.txt', 'r') as file:
    for line in file:
        x, y, size, orientation = line.strip().strip('()').split(',')
        x = int(x)
        y = int(y)
        size = int(size)

        # Postavite vrednosti u matricu u zavisnosti od orijentacije
        if orientation == 'v':
            for i in range(size):
                 n[x+i][y] = 'B'
        else:
            for j in range(size):
                n[x][y+j] = 'B'


# Ispis matrice
for i in range(7):
    for j in range(7):
        print(matrica[i][j], end=' ')
    print()

# %%

n = [[' ' for i in range(7)] for j in range(7)]

with open('brodovi.txt', 'r') as file:
    for line in file:
        x, y, size, orientation = line.strip().strip('()').split(',')
        x, y, size = int(x), int(y), int(size)
        if orientation == 'v':
            for i in range(size):
                n[x+i][y] = 'B'
        else:
            for j in range(size):
                n[x][y+j] = 'B'

# %%