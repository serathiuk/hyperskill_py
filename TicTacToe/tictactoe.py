ALLOWED_NUMBERS = ['1', '2', '3']
ALLOWED_CHARS_PLAYER = 'xXoO0'

cells = '         '
lines = [list(cells[i:i + 3]) for i in range(0, 9, 3)]
current_player = 'X'


def print_should_numbers():
    print('You should enter numbers!')


def print_coordinates_error():
    print('Coordinates should be from 1 to 3!')


def print_cell_occupied():
    print('This cell is occupied! Choose another one')


def print_board():
    print('---------')
    for l in lines:
        print('|', l[0], l[1], l[2], '|')
    print('---------')


def convert_and_validate_char(char):
    if not char.isdigit():
        print_should_numbers()
        return None
    elif char not in ALLOWED_NUMBERS:
        print_coordinates_error()
        return None
    else:
        return int(char)


def convert_typed_x(typed):
    if typed == 1:
        return 2
    elif typed == 2:
        return 1
    elif typed == 3:
        return 0
    else:
        return -1


def convert_typed_y(typed):
    return typed - 1


def ask_coordinates():
    while True:
        coordinates = input('Enter the coordinates:')
        if len(coordinates) != 3:
            print_should_numbers()
            continue

        typed_x = convert_and_validate_char(coordinates[0])
        if typed_x is None:
            continue

        typed_y = convert_and_validate_char(coordinates[2])
        if typed_y is None:
            continue

        converted_x = convert_typed_x(typed_y)
        converted_y = convert_typed_y(typed_x)

        current_position = lines[converted_x][converted_y]
        if current_position in ALLOWED_CHARS_PLAYER:
            print_cell_occupied()
            continue

        return [converted_x, converted_y]


def move(x_position, y_position, player):
    global lines

    if player not in ALLOWED_CHARS_PLAYER:
        print('Invalid char.')
        return False

    lines[x_position][y_position] = player
    return True


def ask_and_move():
    global current_player
    x, y = ask_coordinates()
    move(x, y, current_player)
    current_player = 'O' if current_player == 'X' else 'X'


def get_total_blanks():
    total_blanks = 0
    for l in lines:
        total_blanks += len([b for b in l if b in ' _'])
    return total_blanks


def is_full():
    return get_total_blanks() == 0


def get_total_victories(player):
    victories = 0
    for l in lines:
        total = len([x for x in l if x == player])
        if total == 3:
            victories += 1

    if lines[0][0] == lines[1][1] == lines[2][2] == player:
        victories += 1

    if lines[0][2] == lines[1][1] == lines[2][0] == player:
        victories += 1

    return victories


def get_victories():
    return [get_total_victories('X'), get_total_victories('O')]


def check_if_finished_and_status():
    victories_x, victories_o = get_victories()
    if (victories_x + victories_o) > 1:
        return [True, 'Impossible']
    elif victories_x == 1:
        return [True, 'X wins']
    elif victories_o == 1:
        return [True, 'O wins']
    elif is_full():
        return [True, 'Draw']
    else:
        return [False, '']


def main():
    print_board()
    while True:
        ask_and_move()
        print_board()
        finished, status = check_if_finished_and_status()
        if finished:
            print(status)
            break


main()
