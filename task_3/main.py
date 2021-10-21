from figures_2d import *
from figures_3d import *


fig_list = ["Круг", "Квадрат", "Прямоугольник", "Треугольник", "Трапеция", "Ромб",
            "Сфера", "Куб", "Параллелепипед", "Пирамида", "Цилиндр", "Конус"]


fig_dict = {"Круг": Circle, "Квадрат": Square, "Прямоугольник": Rectangle,
            "Треугольник": Triangle, "Трапеция": Trapezoid, "Ромб": Rhombus,
            "Сфера": Sphere, "Куб": Cube, "Параллелепипед": Parallelepiped,
            "Пирамида": Pyramid, "Цилиндр": Cylinder, "Конус": Cone}


print("Здравствуйте! Вас приветствует Геометрический калькулятор!")
# TODO добавить выбор функционала
print("Список доступных фигур:")
for idx, figure in enumerate(fig_list, 1):
    print(f"{idx}. {figure}")

while True:
    try:
        fig_idx = int(input("Введите номер выбранной фигуры: "))
        assert 1 <= fig_idx <= len(fig_list)
        break
    except ValueError:
        print("Неверное значение. Повторите ввод.")
    except AssertionError:
        print("Введенный номер не соответствует диапазону допустимых значений.")

# print(f'Выбранная Вами фигура - "{fig_list[fig_idx - 1]}"')
print(f'Выбранная Вами фигура - "{fig_dict[fig_list[fig_idx - 1]]}"')
# TODO добавить введение сторон фигуры
for var in fig_dict[fig_list[fig_idx - 1]].__annotations__:
    print(var)
print(fig_dict[fig_list[fig_idx - 1]])
# TODO добавить список операций для фигур
print("Для данной фигуры доступны следующие операции:")

user_fig = fig_dict[fig_list[fig_idx - 1]]()
print(user_fig)
