class Board:

    board = [[" " for row in range(3)] for line in range(3)]

    def display_board(self):
        print("---------")
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                print(str(self.board[i][j]) + " ", end="")
            print("|")
        print("---------")

    def fill_board(self):
        symbols = input("Enter cells: ")
        symbols = symbols.replace("_", " ")
        char_counter = 0
        for i in range(3):
            for j in range(3):
                self.board[i][j] = symbols[char_counter]
                char_counter += 1

    def check_state(self):
        X_count = 0
        O_count = 0
        X_wins = False
        O_wins = False
        for i in range(3):
            string_row = ""
            string_column = ""
            string_diagonal = ""
            string_other_diagonal = ""
            for j in range(3):
                if self.board[i][j] == "X":
                    X_count += 1
                elif self.board[i][j] == "O":
                    O_count += 1
                string_row += self.board[i][j]
                string_column += self.board[j][i]
                string_diagonal += self.board[j][j]
                string_other_diagonal += self.board[j][len(self.board) - 1 - j]

            if string_row == "XXX" or string_column == "XXX" or string_diagonal == "XXX" or string_other_diagonal == "XXX":
                X_wins = True
            elif string_row == "OOO" or string_column == "OOO" or string_diagonal == "OOO" or string_other_diagonal == "OOO":
                O_wins = True

        if abs(X_count - O_count) > 1 or (X_wins and O_wins):
            print("Impossible")
        elif X_wins:
            print("X wins")
        elif O_wins:
            print("O wins")
        elif X_count + O_count == 9:
            print("Draw")

    # (1, 1) (1, 2) (1, 3)
    # (2, 1) (2, 2) (2, 3)
    # (3, 1) (3, 2) (3, 3)

    def make_move(self, user_input, symbol):
        x, y = user_input.split()
        is_occupied = False
        is_not_coordinate = False

        try:
            x = int(x)
            y = int(y)
            if (x < 1 or x > 3) or (y < 0 or y > 3):
                is_not_coordinate = True
            
        except ValueError:
            print("You should enter numbers!")
            return False

        if not is_not_coordinate:
            if self.board[x - 1][y - 1] != " ":
                is_occupied = True
            else:
                self.board[x - 1][y - 1] = symbol
                return True

        if is_not_coordinate:
            print("Coordinates should be from 1 to 3!")
        elif is_occupied:
            print("This cell is occupied! Choose another one!")


board = Board()
board.display_board()
move_counter = 0
symbol = ""

while move_counter < 9:
    if move_counter % 2 == 0:
        symbol = "X"
    else:
        symbol = "O"
    command = input("Enter the coordinates: ")
    if board.make_move(command, symbol):
        move_counter += 1
        board.display_board()
        board.check_state()
