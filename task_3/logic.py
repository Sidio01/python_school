from typing import Tuple
from abstract_figures import Figure
from figures_2d import *
from figures_3d import *


fig_list = ["Круг", "Квадрат", "Прямоугольник", "Треугольник", "Трапеция", "Ромб",
            "Сфера", "Куб", "Параллелепипед", "Пирамида", "Цилиндр", "Конус"]

fig_dict = {"Круг": Circle, "Квадрат": Square, "Прямоугольник": Rectangle,
            "Треугольник": Triangle, "Трапеция": Trapezoid, "Ромб": Rhombus,
            "Сфера": Sphere, "Куб": Cube, "Параллелепипед": Parallelepiped,
            "Пирамида": Pyramid, "Цилиндр": Cylinder, "Конус": Cone}

action_list = ["Выбрать другую фигуру.",
               "Изменить параметры ранее выбранной фигуры.",
               "Выполнить другую операцию с ранее выбранной фигурой.",
               "Завершить работу."]


def print_list_of_available_figures() -> None:
    """Вывод на печать списка доступных фигур."""
    print("Список доступных фигур:")
    for idx, figure in enumerate(fig_list, 1):
        print(f"{idx}. {figure}")


def select_figure() -> None:
    """Выбор фигуры."""
    while True:
        try:
            fig_idx = int(input("Введите номер выбранной фигуры: "))
            assert 1 <= fig_idx <= len(fig_list)
            print()
            return fig_idx
        except ValueError:
            print("Неверное значение. Повторите ввод.")
        except AssertionError:
            print("Введенный номер не соответствует диапазону допустимых значений.")


def get_figure_parameters(selected_fig: Figure) -> list:
    """Ввод требуемых параметров для выбранной фигуры."""
    print("Введите требуемые значения для данной фигуры.")
    print("Обратите внимание, в скобках указан тип требуемого значения.")
    while True:
        try:
            fig_vars = []
            for var in selected_fig.__annotations__:
                input_var = float(
                    input(f'Введите значение {var} ({selected_fig.__annotations__[var]}): '))
                assert input_var > 0
                fig_vars.append(input_var)
            print()
            return fig_vars
        except ValueError:
            print("Неверное значение. Повторите ввод.")
        except AssertionError:
            print("Введенный номер не соответствует диапазону допустимых значений.")


def get_methods_list(selected_fig: Figure) -> tuple((list, int)):
    """Получение списка доступных операций над фигурой."""
    print("Для данной фигуры доступны следующие операции:")
    method_list = [method for method in dir(selected_fig) if (
        method.startswith('__') or method.startswith('_')) is False]
    for idx, method in enumerate(method_list, 1):
        print(f'{idx}. {method} - {getattr(selected_fig, method).__doc__}')
    while True:
        try:
            operation_idx = int(input("Введите номер выбранной операции: "))
            assert 1 <= operation_idx <= len(method_list)
            print()
            return method_list, operation_idx
        except ValueError:
            print("Неверное значение. Повторите ввод.")
        except AssertionError:
            print("Введенный номер не соответствует диапазону допустимых значений.")


def execute_method(user_fig: Figure, method_list: list, operation_idx: int) -> None:
    """Выполнение выбранной операции."""
    result = getattr(user_fig, method_list[operation_idx - 1])()
    print(f'Результат выбранной операции - {result}\n')


def determine_next_action() -> int:
    """Выбор варианта дальнейшего развития событий."""
    print("Выберите дальнейшее действие:")
    for idx, action in enumerate(action_list, 1):
        print(f'{idx}. {action}')
    while True:
        try:
            action_idx = int(input("Введите номер выбранного действия: "))
            assert 1 <= action_idx <= 4
            print()
            return action_idx
        except ValueError:
            print("Неверное значение. Повторите ввод.")
        except AssertionError:
            print("Введенный номер не соответствует диапазону допустимых значений.")
