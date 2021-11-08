import random

dominoes_seg = []
dominoes = []

for i in range(0, 7):
    for j in range(0, 7):
        dominoes_seg.append([i, j])

dominoes_seg = [sorted(item) for item in dominoes_seg]
dominoes_seg = list(set(map(tuple, dominoes_seg)))

for d in dominoes_seg:
    dominoes.append(list(d))

stock = []
player_stock = []
ai_stock = []

for i in range(14):
    index = random.randint(0, len(dominoes) - 1)
    stock.append(dominoes[index])
    dominoes.pop(index)

for i in range(7):
    index_1 = random.randint(0, len(dominoes) - 1)
    player_stock.append(dominoes[index_1])
    dominoes.pop(index_1)

    index_2 = random.randint(0, len(dominoes) - 1)
    ai_stock.append(dominoes[index_2])
    dominoes.pop(index_2)


def starting_player(player_set, ai_set):
    max_domino_player = [0, 0]
    max_domino_ai = [0, 0]
    player_starts = False

    for domino in player_set:
        if domino[0] + domino[1] > max_domino_player[0] + max_domino_player[1]:
            max_domino_player = domino

    for domino in ai_set:
        if domino[0] + domino[1] > max_domino_ai[0] + max_domino_ai[1]:
            max_domino_ai = domino

    if max_domino_player > max_domino_ai:
        player_set.remove(max_domino_player)
        max_domino = max_domino_player
    else:
        ai_set.remove(max_domino_ai)
        max_domino = max_domino_ai
        player_starts = True

    return max_domino, player_starts


def player_move(player_set, game_set, board):
    while True:
        try:
            command = int(input())
        except ValueError:
            print("Invalid input. Please try again.")
            print_interface()
            print("\nStatus: It's your turn to make a move. Enter your command.")
        else:
            domino_end = board[-1]
            domino_start = board[0]
            if 0 < command <= len(player_set):
                domino_to_insert = player_set[command - 1]
                if domino_end[1] == domino_to_insert[0]:
                    board.append(domino_to_insert)
                    player_set.remove(domino_to_insert)
                    break
                elif domino_end[1] == domino_to_insert[1]:
                    player_set.remove(domino_to_insert)
                    domino_to_insert.reverse()
                    board.append(domino_to_insert)
                    break
            elif -len(player_set) - 1 < command < 0:
                domino_to_insert = player_set[abs(command) - 1]
                if domino_start[0] == domino_to_insert[1]:
                    board.insert(0, domino_to_insert)
                    player_stock.remove(domino_to_insert)
                    break
                elif domino_start[0] == domino_to_insert[0]:
                    player_set.remove(domino_to_insert)
                    domino_to_insert.reverse()
                    board.insert(0, domino_to_insert)
                    break
            elif command == 0:
                ran_index = random.randint(0, len(game_set) - 1)
                if len(game_set) == 0:
                    print("Status: The game is over. The computer won!")
                    return False
                domino_to_add_player = game_set[ran_index]
                player_set.append(domino_to_add_player)
                game_set.remove(domino_to_add_player)
                break
            else:
                print("Invalid input. Please try again.")
                print_interface()
                print("\nStatus: It's your turn to make a move. Enter your command.")


def print_interface():
    string = ''
    print("=" * 70)
    print("Stock size: " + str(len(stock)))
    print("Computer pieces: " + str(len(ai_stock)))
    print()

    if len(domino_snake) >= 6:
        print(str(domino_snake[0]) + str(domino_snake[1]) + str(domino_snake[2]) + "..." + str(domino_snake[-3]) + str(domino_snake[-2]) + str(domino_snake[-1]))
    else:
        for d in domino_snake:
            string += str(d)
        print(string)
    print()
    print("Your pieces:")
    for i in range(len(player_stock)):
        print(str(i + 1) + ":" + str(player_stock[i]))


def ai_move(ai_set, game_set, board):
    while True:
        ai_index = random.randint(-len(ai_set), len(ai_set) - 1)
        domino_start = board[0]
        domino_end = board[-1]
        if 0 < ai_index < len(ai_set):
            domino_to_insert = ai_set[ai_index]
            if domino_end[1] == domino_to_insert[0]:
                board.append(domino_to_insert)
                ai_set.remove(domino_to_insert)
                break
            elif domino_end[1] == domino_to_insert[1]:
                ai_set.remove(domino_to_insert)
                domino_to_insert.reverse()
                board.append(domino_to_insert)
                break
        elif -len(ai_set) - 1 < ai_index < 0:
            domino_to_insert = ai_set[abs(ai_index) - 1]
            if domino_start[0] == domino_to_insert[1]:
                board.insert(0, domino_to_insert)
                ai_set.remove(domino_to_insert)
                break
            elif domino_start[0] == domino_to_insert[0]:
                ai_set.remove(domino_to_insert)
                domino_to_insert.reverse()
                board.insert(0, domino_to_insert)
                break
        elif ai_index == 0:
            random_ = random.randint(0, len(game_set) - 1)
            random_domino_ai = game_set[random_]
            ai_set.append(random_domino_ai)
            game_set.remove(random_domino_ai)
            break


def check_condition(ai_set, player_set, board):
    starting = board[0]
    ending = board[len(board) - 1]
    counter = 0
    if len(ai_set) == 0:
        print("Status: The game is over. The computer won!")
        return True
    elif len(player_set) == 0:
        print("Status: The game is over. You won!")
        return True
    elif starting[0] == ending[1] and len(board) > 1:
        for b in board:
            if b[0] or b[1] == starting[0]:
                counter += 1
        if counter == 8:
            print("Status: The game is over. It's a draw!")
            return True


staring_domino = starting_player(player_stock, ai_stock)
domino_snake = [staring_domino[0]]
player_moves = staring_domino[1]
is_running = True

while is_running:
    print_interface()
    if player_moves:
        if check_condition(ai_stock, player_stock, domino_snake):
            break
        print("\nStatus: It's your turn to make a move. Enter your command.")
        player_move(player_stock, stock, domino_snake)
        is_running = player_move(player_stock, stock, domino_snake)
        player_moves = False
    elif not player_moves:
        if check_condition(ai_stock, player_stock, domino_snake):
            break
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        ai_move(ai_stock, stock, domino_snake)
        input()
        player_moves = True

