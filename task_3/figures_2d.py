from abstract_figures import Figure_2D


class Circle(Figure_2D):
    """Круг."""
    # Характеристики: Радиус

    # Площадь круга = пи * радиус**2
    # Периметр (длина окружности) = 2* пи * радиус
    pass


class Square(Figure_2D):
    """Квадрат."""
    x: int
    # Характеристики: одна сторона (все равны)

    # Площадь = сторона**2
    # Периметр = 2* пи * радиус
    # Диагональ = 2 ** 0,5 * сторона
    # Диагонали делят углы пополам
    # Диагонали пересекаются под прямым углом
    def __init__(self, x: int) -> None:
        super().__init__()
        self.x = x

    def area(self):
        return self.x ** 2

    def perimeter(self):
        return self.x * 4


class Rectangle(Figure_2D):
    """Прямоугольник."""
    pass


class Triangle(Figure_2D):
    """Треугольник."""
    pass


class Trapezoid(Figure_2D):
    """Трапеция."""
    pass


class Rhombus(Figure_2D):
    """Ромб."""
    pass
