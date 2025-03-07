from algos import initial_state, player, actions, result, terminal, winner, minimax, X, O, EMPTY

def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.
    """
    for i, row in enumerate(board):
        # Convert None to ' ' for display
        display_row = [' ' if cell is EMPTY else cell for cell in row]
        print(f" {display_row[0]} | {display_row[1]} | {display_row[2]} ")
        if i < 2:
            print("-----------")

def main():
    print("Welcome to Tic Tac Toe against AI!")
    
    # Let the user choose their symbol
    user = input("Choose your symbol (X/O): ").upper()
    while user not in [X, O]:
        user = input("Invalid choice. Choose X or O: ").upper()
    ai = O if user == X else X
    
    board = initial_state()
    
    while not terminal(board):
        print("\nCurrent board:")
        print_board(board)
        current_player = player(board)
        
        if current_player == user:
            # User's turn
            print("Your turn!")
            valid_actions = actions(board)
            while True:
                try:
                    move = input("Enter row and column (1-3 each, space-separated): ").strip().split()
                    if len(move) != 2:
                        raise ValueError("Please enter exactly two numbers.")
                    row = int(move[0]) - 1  # Convert to 0-based index
                    col = int(move[1]) - 1
                    if (row, col) in valid_actions:
                        board = result(board, (row, col))
                        break
                    else:
                        print("Invalid move. Choose an empty cell within 1-3.")
                except ValueError as e:
                    print(f"Invalid input: {e}")
        else:
            # AI's turn
            print("AI's turn...")
            action = minimax(board)
            board = result(board, action)
    
    # Game over, show final result
    print("\nFinal board:")
    print_board(board)
    game_winner = winner(board)
    if game_winner == user:
        print("Congratulations! You won!")
    elif game_winner == ai:
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
