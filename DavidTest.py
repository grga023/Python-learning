#Create unit test for the function in the file David.py

import unittest
import David

class TestDavid(unittest.TestCase):
    def test_print_board(self):
        board = []
        for i in range(0,7):
            board.append([chr(0x1F7E9)]*7)
        self.assertEqual(David.print_board(board), None)

if __name__ == '__main__':
    unittest.main()

# Path: David.py
# Compare this snippet from David.py:
# for i in range(0,7):
#     wrong.append([chr(0x274C)]*7)

# for i in range(0,7):
#     board.append([chr(0x1F7E9)]*7)

# def print_board(board):
#     for row in board:
#         print (" ".join(row))

# #printasa tablu ne znam da lis te koristili fje ali ti je mnogooo lakse sa njima
# # i iskreno ne predlazem ti da ih sklanjas prevelik je seks bez njih
# print_board(board)

# #%% Pravljenje i upis u file brodovi
# cnt = 0
# ships = 0

# shipRow = [8]
# shipCol = [8]

# x = []
# y = []
# size = []
# orientation = []

# #koristi cvs i reci mu ako te nesto pita da si nasao na netu
# #i da ti je bilo lakse tako da ga koristis

# with open('brodovi.txt','r') as brodici:
#     reader = csv.reader(brodici)
#     for row in reader:
#         x.append(row[0])
#         y.append(row[1])
#         size.append(row[2])
#         orientation.append(row[3])
#         cnt += 1

# for i in range(cnt):
#     x[i] = x[i].replace('(','')
#     orientation[i] = orientation[i].replace(')','')