def display_board(board, separator):
    """Отрисовка игрового поля"""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if len(row[j]) == 1:
                if j == 9:
                    cell_sep = " "
                else:
                    cell_sep = "  | "
            else:
                if j == 9:
                    cell_sep = " "
                else:
                    cell_sep = " | "
            if cell == "X":
                print('\033[92m' + cell + '\033[0m', cell_sep, sep="", end="")
            elif cell == "O":
                print('\033[91m' + cell + '\033[0m', cell_sep, sep="", end="")
            else:
                print('\033[70m' + cell + '\033[0m', cell_sep, sep="", end="")
        print()

        if i == 9:
            pass
        else:
            print(" | ".join(separator))


def clear_screen():
    """Очистка экрана путем добавления пустых строк"""
    print('\n' * 1000)
