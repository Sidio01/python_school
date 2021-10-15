import random
from board import *


marks = ("X", "O")


def player_input():
    """Выбор символа игрока."""
    player = None
    while player not in marks:
        player = input("Выберете игровой символ: X или O: ").upper()

    if player == "X":
        ai = "O"
    else:
        ai = "X"

    return player, ai


def choose_first():
    """Выбор случайным образом стороны с правом первого хода."""
    return marks[random.choice((0, 1))]


def space_check(board, column_position, row_position):
    """Проверка доступности ячейки для постановки символа."""
    return board[row_position][column_position] not in marks


def place_marker(board, marker, column_position, row_position):
    """Постановка символа в ячейку."""
    board[row_position][column_position] = marker


def turn_switch(mark):
    """Осуществление перехода хода."""
    return "O" if mark == "X" else "X"


def mark_type_switch(player_type):
    """Изменение типа стороны"""
    return "ai" if player_type == "player" else "player"


def full_board_check(board):
    """Проверка на отсутствие пустых ячеек на игровом поле."""
    draw_check = []
    for row in board:
        draw_check += row
    return len(set(draw_check)) == 2


def check_column(board, mark, column_position):
    """Проверка столбца, в ячейку которого был совершен последний ход, на соответствие условиям поражения."""
    counter = 0
    for row in board:
        if row[column_position] == mark:
            counter += 1
        else:
            counter = 0
        if counter == 5:
            return True
    return False


def check_row(board, mark, row_position):
    """Проверка строки, в ячейку которой был совершен последний ход, на соответствие условиям поражения."""
    counter = 0
    for cell in board[row_position]:
        if cell == mark:
            counter += 1
        else:
            counter = 0
        if counter == 5:
            return True
    return False


def check_diagonal(board, mark, column_position, row_position):
    """Проверка главной диагонали, в ячейку которой был совершен последний ход, на соответствие условиям поражения"""
    counter = 0
    bias = min(column_position, row_position)
    row_bias = bias
    for row in board[row_position - row_bias:]:
        if column_position - bias > 9:
            break
        if row[column_position - bias] == mark:
            counter += 1
        else:
            counter = 0
        if counter == 5:
            return True
        bias -= 1
    return False


def check_reverse_diagonal(board, mark, column_position, row_position):
    """Проверка обратной диагонали, в ячейку которой был совершен последний ход, на соответствие условиям поражения"""
    counter = 0
    bias = max(column_position, row_position)
    while True:
        if (column_position + bias) <= 9 and (row_position - bias) >= 0:
            break
        bias -= 1
    row_bias = bias
    for row in board[row_position - row_bias:]:
        if (column_position + bias) < 0:
            break
        if row[column_position + bias] == mark:
            counter += 1
        else:
            counter = 0
        if counter == 5:
            return True
        bias -= 1
    return False


def lost_check(board, mark, column_position, row_position):
    """Возвращает логическое значение проиграл ли игрок с передаваемым символом."""
    return any([check_column(board, mark, column_position),
                check_row(board, mark, row_position),
                check_diagonal(board, mark, column_position, row_position),
                check_reverse_diagonal(board, mark, column_position, row_position)])


def check_game_finish(board, mark, column_position, row_position, player_type):
    """Проверка на завершение игры."""
    if lost_check(board, mark, column_position, row_position):
        clear_screen()
        if player_type == "ai":
            print("Итог игры: Вы победили!")
        else:
            print("Итог игры: Вы проиграли!")
        return True
    if full_board_check(board):
        clear_screen()
        print("Итог игры: Ничья")
        return True

    return False
