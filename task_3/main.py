from logic import *


action_idx = 1

print("Здравствуйте! Вас приветствует Геометрический калькулятор!\n")

while True:
    if action_idx == 1:  # Выбрать фигуру
        print_list_of_available_figures()
        fig_idx = select_figure()
        selected_fig = fig_dict[fig_list[fig_idx - 1]]
        fig_vars = get_figure_parameters(selected_fig)
        user_fig = selected_fig(*fig_vars)
        method_list, operation_idx = get_methods_list(selected_fig)
        execute_method(user_fig, method_list, operation_idx)
        action_idx = determine_next_action()

    elif action_idx == 2:  # Изменить параметры ранее выбранной фигуры
        fig_vars = get_figure_parameters(selected_fig)
        user_fig = selected_fig(*fig_vars)
        action_idx = determine_next_action()
    
    elif action_idx == 3:  # Выполнить другую операцию с ранее выбранной фигурой
        method_list, operation_idx = get_methods_list(selected_fig)
        execute_method(user_fig, method_list, operation_idx)
        action_idx = determine_next_action()

    else:
        print("Спасибо за использование Геометрического калькулятора!")
        break
