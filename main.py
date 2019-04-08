board = ['_'] * 9

def main():
    print_board()
    while victorycheck() == 0 and board_check():
        player_a()
        if victorycheck() != 0:
            break
        player_b()
        victorycheck()
    whowon(victorycheck)
    if not board_check():
        print("Remis")
    # Tutaj chyba jest trochę bałagan.

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    # Przyznaję zajebane z neta.

def player_a():
    print("TURA X")
    x = input('Wybierz pole od 1 do 9')
    x = int(x) - 1
    if board[x] != 'O':
        board[x] = 'X'
        print_board()
    else:
        print("Pole już zajęte, tracisz turę")
    # Pewnie gdyby zrobić osobną funkcję do kontroli pola byłoby lepiej,
    # ale tak wymyśliłem najpierw i działało, więc nie zmieniałem.

def player_b():
    print("TURA Y")
    o = input('Wybierz pole od 1 do 9')
    o = int(o) - 1
    if board[o] != 'X':
        board[o] = 'O'
        print_board()
    else:
        print("Pole już zajęte, tracisz turę")
    # j.w.

def victorycheck():
    if board[0] == board[1] == board[2] != '_':
        return board[0]
    if board[3] == board[4] == board[5] != '_':
        return board[3]
    if board[6] == board[7] == board[8] != '_':
        return board[6]
    # horizontal check
    if board[0] == board[3] == board[6] != '_':
        return board[0]
    if board[1] == board[4] == board[7] != '_':
        return board[1]
    if board[2] == board[5] == board[8] != '_':
        return board[8]
    # vertical check
    if board[0] == board[4] == board[8] != '_':
        return board[0]
    if board[2] == board[4] == board[6] != '_':
        return board[2]
    # diagonal check
    else:
        return 0
    # Masakrycznie młotkowa metoda, na pewno da się to zrobić mniej barbarzyńsko. Niestety, tylko na to wpadłem.

def whowon(victorycheck):

    if victorycheck != 0:
        print("Wygrywa: ")
        print(victorycheck())
    else:
        return 0
    # Da się na pewno w jednej linii, ale konkatenacja mi nie wychodziła i trochę mam to w zadzie.

def board_check():

    while '_' in board:
        return True
    # To też dosyć mało eleganckie chyba, ale działa.

main()