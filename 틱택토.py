import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # 가로, 세로, 대각선 검사
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "] #리스트 함축 이중 for문 조건문



def player_move(board):
            while True:
                move = input("당신의 차례 (행과 열을 띄어쓰기로 구분하여 입력, 예: 1 2): ")
                parts = move.split()
                if len(parts) == 2 and all(p.isdigit() for p in parts):  # 입력값이 숫자인지 확인
                    row, col = map(int, parts)
                    if 0 <= row < 3 and 0 <= col < 3:
                        if board[row][col] == " ":
                            board[row][col] = "X"
                            break
                        else:
                            print("이미 선택된 자리입니다. 다시 입력하세요.")
                    else:
                        print("잘못된 입력입니다. 0~2 사이의 숫자로 다시 입력하세요.")
                else:
                    print("올바른 형식으로 입력해주세요 (예: 1 2).")


def computer_move(board):
    row, col = random.choice(get_available_moves(board))
    board[row][col] = "O"
    print(f"컴퓨터가 ({row}, {col}) 위치에 놓았습니다.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            computer_move(board)

        print_board(board)

        if check_winner(board, "X"):
            print("축하합니다! 당신이 승리했습니다!")
            return
        elif check_winner(board, "O"):
            print("컴퓨터가 승리했습니다!")
            return

    print("무승부입니다!")


if __name__ == "__main__":
    main()
