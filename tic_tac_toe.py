def print_board(board):
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':  # row
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':  # column
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':  # diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':  # diagonal
        return True
    return False

board = [[' ' for _ in range(3)] for _ in range(3)]
while True:
    print_board(board)
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))
    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'
    if check_win(board):
        print_board(board)
        print("당신이 이겼습니다!")
        break
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
    if check_win(board):
        print_board(board)
        print("컴퓨터가 이겼습니다!")
        break