import random
from mechanics import *


def player_turn(board):
    """Расчет хода игрока."""
    position = 0
    column_position = 0
    row_position = 0

    while position not in [num for num in range(1, 101)]:
        try:
            position = int(input("Введите число от 1 до 100: "))
            assert position > 0
            column_position = (position - 1) % 10
            row_position = (position - 1) // 10
            if column_position >= 10 or row_position >= 10:
                raise ValueError
            if not space_check(board, column_position, row_position):
                position = 0
                raise KeyError

        except ValueError:
            print("Некорректное значение.")
        except KeyError:
            print("Ячейка занята. Выберете другую ячейку.")
        except AssertionError:
            print("Некорректное значение.")

    return column_position, row_position


def ai_turn(board, mark):
    """Расчет хода компьютера."""
    position = 0
    column_position = 0
    row_position = 0
    good_turns = []
    available_turns = []

    for x, row in enumerate(board):
        for y, _ in enumerate(row):
            if space_check(board, y, x):
                curr_value = board[x][y]
                board[x][y] = mark
                turn = lost_check(board, mark, y, x)
                if not turn:
                    good_turns.append((y, x))
                board[x][y] = curr_value
                available_turns.append((y, x))

    if good_turns:
        position = random.choice(good_turns)
    else:
        position = random.choice(available_turns)
    column_position = position[0]
    row_position = position[1]

    return column_position, row_position
