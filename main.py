# Tic Tac Toe Game
while continue_game := True:
    list = [["-","-","-"]for _ in range(3)]
    def print_board():
        for row in list:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner():
        # Check rows
        for row in list:
            if row[0] == row[1] == row[2] and row[0] != "-":
                return row[0]
        # Check columns
        for col in range(3):
            if list[0][col] == list[1][col] == list[2][col] and list[0][col] != "-":
                return list[0][col]
        # Check diagonals
        if list[0][0] == list[1][1] == list[2][2] and list[0][0] != "-":
            return list[0][0]
        if list[0][2] == list[1][1] == list[2][0] and list[0][2] != "-":
            return list[0][2]
        return None

    current_player = "X"
    turns = 0

    print("Welcome to Tic Tac Toe!")
    while turns < 9:
        print_board()
        print(f"Player {current_player}'s turn.")

        try:

            row_input= int(input("Enter row (1, 2, 3): "))
            col_input = int(input("Enter column (1, 2, 3): "))
            row, col = row_input - 1, col_input - 1

            if list[row][col] == "-":
                list[row][col] = current_player
                turns += 1
                winner = check_winner()
                if winner:
                    print_board()
                    print(f"Player {winner} wins!")
                    break
                current_player = "O" if current_player == "X" else "X"
            elif row not in range(1, 4) or col not in range(1, 4):
                print("Invalid input. Please enter numbers between 1 and 3.")

            else:
                print("Cell already taken. Try again.")

        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3.")
    if not winner:
        print_board()
        print("It's a tie!")
