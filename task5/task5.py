def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): ")) - 1
            
            if move < 0 or move > 8:
                print("Invalid position. Choose 1-9.")
            elif board[move] != " ":
                print("Position already taken. Try again.")
            else:
                return move
                
        except ValueError:
            print("Please enter a number.")


def main():
    board = [" "] * 9

    # Player chooses symbol
    player1 = input("Player 1, choose X or O: ").upper()
    while player1 not in ["X", "O"]:
        player1 = input("Invalid choice. Choose X or O: ").upper()

    player2 = "O" if player1 == "X" else "X"

    current_player = player1

    print_board(board)

    while True:
        move = get_move(board, current_player)
        board[move] = current_player

        print_board(board)

        # Check winner
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        # Check draw
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    main()