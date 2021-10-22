from math import pi
from abstract_figures import Figure


class Circle(Figure):
    """Круг."""
    r: float

    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        """Вычисление площади."""
        return pi * self.r ** 2

    def perimeter(self) -> float:
        """Вычисление периметра (длины окружности)."""
        return 2 * pi * self.r

    def diameter(self) -> float:
        """Вычисление диаметра."""
        return self.r * 2


class Square(Figure):
    """Квадрат."""
    x: float

    def __init__(self, x: float) -> None:
        self.x = x

    def area(self) -> float:
        """Вычисление площади."""
        return self.x ** 2

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self.x * 4
    
    def diagonal(self) -> float:
        """Вычисление длины диагонали."""
        return 2 ** 0.5 * self.x


class Rectangle(Square):
    """Прямоугольник."""
    x: float
    y: float
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x)
        self.y = y

    def area(self) -> float:
        """Вычисление площади."""
        return self.x * self.y

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return (self.x + self.y) * 2

    def diagonal(self) -> float:
        """Вычисление длины диагонали."""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def radius(self) -> float:
        """Вычисление радиуса описанной окружности."""
        return (self.x ** 2 + self.y ** 2) ** 0.5 / 2


class Triangle(Figure): #TODO описать класс
    """Треугольник."""
    pass


class Trapezoid(Figure): #TODO описать класс
    """Трапеция."""
    pass


class Rhombus(Figure): #TODO описать класс
    """Ромб."""
    pass
