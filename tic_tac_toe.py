import sys
from minimax import find_best_move, check_winner

def print_board(board):
    """
    Prints the current state of the board.
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def main():
    print("Welcome to Tic-Tac-Toe AI!")
    print("Human (X) vs AI (O)")
    print("Positions are numbered 1-9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    while True:
        board = [' '] * 9
        current_player = 'X' # Human starts
        
        while True:
            print_board(board)
            winner = check_winner(board)
            
            if winner:
                if winner == 'Draw':
                    print("It's a Draw!")
                else:
                    print(f"Player {winner} wins!")
                break
            
            if current_player == 'X':
                try:
                    move = int(input("Your turn! Enter a position (1-9): ")) - 1
                    if move < 0 or move > 8 or board[move] != ' ':
                        print("Invalid move. Try again.")
                        continue
                    board[move] = 'X'
                    current_player = 'O'
                except ValueError:
                    print("Please enter a number between 1 and 9.")
            else:
                print("AI is thinking...")
                move = find_best_move(board)
                if move != -1:
                    board[move] = 'O'
                current_player = 'X'
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
