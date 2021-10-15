import time
from board import *
from mechanics import *
from turns import *


play_board = [[str(i * 10 + j) for j in range(1, 11)] for i in range(0, 10)]
separator = ["--" for _ in range(10)]

print("Добро пожаловать в обратные крестики-нолики 10х10")
print("Правила изменены: Цель игры - НЕ собрать 5 в ряд")

player_mark, ai_mark = player_input()
current_mark = choose_first()

if current_mark == player_mark:
    player_type = "player"
else:
    player_type = "ai"

if player_type == "player":
    print("Вы ходите первым")
else:
    print("Первым ходит компьютер")
time.sleep(1)

while True:
    display_board(play_board, separator)

    if current_mark == player_mark:
        column_position, row_position = player_turn(play_board)
        place_marker(play_board, current_mark, column_position, row_position)
    else:
        column_position, row_position = ai_turn(play_board, current_mark)
        place_marker(play_board, current_mark, column_position, row_position)

    if check_game_finish(play_board, current_mark, column_position, row_position, player_type):
        display_board(play_board, separator)
        print("Спасибо за игру!")
        break
    else:
        current_mark = turn_switch(current_mark)
        player_type = mark_type_switch(player_type)
    clear_screen()