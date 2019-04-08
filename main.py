import numpy as np
import string

# def main():
#     template = initialize()
#     show_plain(template)
#     input_gracza()
#
# def show_plain(template):
#     for i in range(3):
#         for j in range(3):
#             print(template[i][j], end='')
#         print(' ')
#
# def initialize():
#     template = [['x' for i in range(3)] for i in range(3)]
#     return template
#
# def input_gracza():
#     print("Tura X")
#     choice = input("wybierz pole: ")
#     print(choice)

# def main():
#     template = initialize()
#     show_plain(template)
#     input_gracza(template)
#
# def show_plain(template):
#     for x in range(3):
#         for y in range(3):
#             print(template[0], end='')
#         print(' ')
#
# def initialize():
#     template = [9]
#     return template
#
# def input_gracza():
#     print("Tura X")
#     choice = input("wybierz pole (od 1 do 9): ")
#     choice = int(choice)
#     # template.pop(choice)
#     # template.insert(choice, 'x')
#     return choice


# def input_gracza_2():
#
# def whowon():
#
# def zabezpieczenie():
#
# def zmianagracza():

board = ['_'] * 9

def main():
    while whowon != 0:
        print_board
        player_a()
        player_b()
        victorycheck()
    print("Wygrał: " + victorycheck)

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_a():
    print("TURA X")
    x = input('Pick a number from 1-9')
    x = int(x) - 1
    if board[x] != 'O':
        board[x] = 'X'
        print_board()
    else:
        print("Pole już zajęte, tracisz turę")

def player_b():
    print("TURA Y")
    o = input('Pick a number from 1-9')
    o = int(o) - 1
    if board[o] != 'X':
        board[o] = 'O'
        print_board()
    else:
        print("Pole już zajęte, tracisz turę")

def victorycheck():
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return 1
    if board[3] == board[4] == board[5]:
        return board[3]
    if board[6] == board[7] == board[8]:
        return board[6]
    else:
        return 0
def whowon(victorycheck):

    if victorycheck != 0:
        return victorycheck
    else:
        return 0


main()