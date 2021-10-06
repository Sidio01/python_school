from math import inf


def calculate_distance(x1, x2, y1, y2):
    """Расчет расстояния между точками"""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def find_shortest_distance(points_list):
    """Точный поиск (полным перебором) кратчайшего маршрута для 5 пунктов с заранее известной точкой старта"""

    assert len(points_list) == 5, "Количество пунктов не равно 5"

    start_point_idx = 0

    a = points_list[start_point_idx]
    points_list = points_list[:start_point_idx] + points_list[start_point_idx + 1:]
    route_list = []

    for b in points_list:
        for c in points_list:
            if b == c:
                continue
            for d in points_list:
                if b == d or c == d:
                    continue
                for e in points_list:
                    if b == e or c == e or d == e:
                        continue
                    ab = calculate_distance(a[0], b[0], a[1], b[1])
                    bc = calculate_distance(b[0], c[0], b[1], c[1])
                    cd = calculate_distance(c[0], d[0], c[1], d[1])
                    de = calculate_distance(d[0], e[0], d[1], e[1])
                    ea = calculate_distance(e[0], a[0], e[1], a[1])
                    res = ab + bc + cd + de + ea
                    route_list.append(
                        (f"{a} -> {b}[{ab}] -> {c}[{ab + bc}] -> {d}[{ab + bc + cd}] -> {e}[{ab + bc + cd + de}] -> {a}[{res}] = {res}", res))

    route_list.sort(key=lambda x: x[1])
    return route_list[0][0]


def approximate_shortest_distance(points_list):
    """Приближенный поиск кратчайшего маршрута"""

    start_point_idx = 0

    visited_points = []
    curr_distance = 0
    ans = str(points_list[start_point_idx])

    def asd_helper(points_list, start_point_idx, last_point_idx, visited_points, distance, answer):
        min_distance = inf

        for i, val in enumerate(points_list):
            if i == start_point_idx or i in visited_points or (i == last_point_idx and len(visited_points) < len(points_list) - 1):
                continue
            x1 = points_list[start_point_idx][0]
            x2 = val[0]
            y1 = points_list[start_point_idx][1]
            y2 = val[1]
            result = calculate_distance(x1, x2, y1, y2)
            if result < min_distance:
                min_distance = result
                next_point_idx = i

        new_distance = distance + min_distance
        visited_points.append(next_point_idx)
        answer += f" -> {(points_list[next_point_idx][0], points_list[next_point_idx][1])}[{new_distance}]"

        if len(points_list) == len(visited_points):
            answer += f" = {new_distance}"
            return answer
        else:
            return asd_helper(points_list, next_point_idx, last_point_idx, visited_points, new_distance, answer)

    return asd_helper(points_list, start_point_idx, start_point_idx, visited_points, curr_distance, ans)


# Список координат адресов
points_list = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]

print(
    f"Кратчайший маршрут методом полного перебора: \n{find_shortest_distance(points_list)}\n")
print(
    f"Кратчайший маршрут методом приближенного поиска: \n{approximate_shortest_distance(points_list)}")