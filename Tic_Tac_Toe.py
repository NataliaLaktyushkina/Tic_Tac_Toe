def check_status(user_input):
    empty_cells = user_input.count('_')
    three_X = False
    three_O = False
    count_X = user_input.count('X')
    count_O = user_input.count('O')
    if (user_input[0:3].count('X') == 3
        or (user_input[3:6].count('X') == 3)
        or (user_input[6:9].count('X') == 3)
        or (user_input[0] == 'X' and user_input[3] == 'X' and user_input[6] == 'X')
        or (user_input[1] == 'X' and user_input[4] == 'X' and user_input[7] == 'X')
        or (user_input[2] == 'X' and user_input[5] == 'X' and user_input[8] == 'X')
        or (user_input[0] == 'X' and user_input[4] == 'X' and user_input[8] == 'X')
        or (user_input[2] == 'X' and user_input[4] == 'X' and user_input[6] == 'X')):
        three_X = True

    if (user_input[0:3].count('O') == 3
        or (user_input[3:6].count('O') == 3)
        or (user_input[6:9].count('O') == 3)
        or (user_input[0] == 'O' and user_input[3] == 'O' and user_input[6] == 'O')
        or (user_input[1] == 'O' and user_input[4] == 'O' and user_input[7] == 'O')
        or (user_input[2] == 'O' and user_input[5] == 'O' and user_input[8] == 'O')
        or (user_input[0] == 'O' and user_input[4] == 'O' and user_input[8] == 'O')
        or (user_input[2] == 'O' and user_input[4] == 'O' and user_input[6] == 'O')):
        three_O = True

    if ((three_X and three_O)
        or abs(count_X - count_O) > 1):
        status = 'Impossible'
    elif three_O:
        status = 'O wins'
    elif three_X:
        status = 'X wins'
    elif not three_X and not three_O and empty_cells:
        status = 'Game not finished'
    else:
        status = 'Draw'

    return status


def print_user_input(user_input):
    print('---------')
    print('| ', end='')
    for symbol in user_input[:3]:
        print(symbol + ' ', end='')
    print('|')
    print('| ', end='')
    for symbol in user_input[3:6]:
        print(symbol + ' ', end='')
    print('|')
    print('| ', end='')
    for symbol in user_input[6:9]:
        print(symbol + ' ', end='')
    print('|')
    print('---------')

# start of the game
print_user_input("_________")

coordinates_correct = False
user_input = '_________'
occupied_cells = user_input[6:] + user_input[3:6] + user_input[0:3]
count = 1
while not coordinates_correct or status == 'Game not finished':
    coordinates = input("Enter the coordinates:").split()
    try:
        list_coordinates = list(map(int, coordinates))
    except ValueError:
        print("You should enter numbers!")
        continue
    coord_index = list_coordinates[0] + (list_coordinates[1] - 1) * 3 - 1

    if not (1 <= list_coordinates[0] <= 3 and 1 <= list_coordinates[1] <= 3):
        print("Coordinates should be from 1 to 3!")
    elif occupied_cells[coord_index] != '_':
        print("This cell is occupied! Choose another one!")
    else:
        list_ocup_cells = list(occupied_cells)
        list_ocup_cells[coord_index] = 'X' if count % 2 == 1 else 'O'
        occupied_cells = "".join(list_ocup_cells)
        user_input = occupied_cells[6:] + occupied_cells[3:6] + occupied_cells[0:3]
        print_user_input(user_input)
        coordinates_correct = True

        status = check_status(user_input)
        if status != 'Game not finished':
            print(status)
            break
        count += 1
