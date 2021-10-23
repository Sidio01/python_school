from math import pi, radians, tan
from abstract_figures import Figure
from figures_2d import *


class Sphere(Circle):
    """Сфера."""
    r: float

    def __init__(self, r: float) -> None:
        super().__init__(r)

    def area(self) -> float:
        """Вычисление площади."""
        return 4 * pi * self.r ** 2

    def volume(self) -> float:
        """Вычисление объема."""
        return 4 / 3 * pi * self.r ** 3


class Cube(Square):
    """Куб."""
    a: float

    def __init__(self, a: float) -> None:
        super().__init__(a)

    def total_area(self) -> float:
        """Площадь боковых сторон."""
        return 6 * self.a ** 2

    def total_perimeter(self) -> float:
        """Вычисление длины ребер."""
        return self.a * 12

    def volume(self) -> float:
        """Вычисление объема."""
        return self.a ** 3


class Parallelepiped(Square):
    """Параллелепипед."""
    a: float
    b: float
    h: float

    def __init__(self, a: float, b: float, h: float) -> None:
        super().__init__(a)
        self.b = b
        self.h = h

    def area(self) -> float:
        """Вычисление площади."""
        return (self.a * self.b + self.b * self.h + self.a * self.h) * 2

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return (self.a + self.b + self.h) * 4

    def diagonal(self) -> float:
        """Вычисление длины диагонали."""
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def main_diagonal(self) -> float:
        """Вычисление главной диагонали."""
        return (self.a ** 2 + self.b ** 2 + self.h ** 2) ** 0.5

    def volume(self) -> float:
        """Вычисление объема."""
        return self.a * self.b * self.h


class Pyramid(Figure):
    """Правильная пирамида."""
    a: float
    n: int
    h: float

    def __init__(self, a: float, n: int, h: float) -> None:
        self.a = a
        self.n = n
        self.h = h

    def area(self) -> float:
        """Вычисление площади."""
        return self.base_area() + self.side_area()

    def base_area(self) -> float:
        """Вычисление площади основания пирамиды."""
        return (self.n * self.a ** 2) / (4 * tan(radians(180 / self.n)))

    def side_area(self) -> float:
        """Вычисление площади боковой поверхности."""
        return self.apothem() * self.a * self.n / 2

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self.n * (self.a + self.edge())

    def volume(self) -> float:
        """Вычисление объема."""
        return self.base_area() * self.h / 3

    def edge(self) -> float:
        """Вычисление ребра пирамиды."""
        return (self.h ** 2 + (self.a / (2 * sin(radians(180 / self.n)))) ** 2) ** 0.5

    def apothem(self) -> float:
        """Вычисление апофемы."""
        return (self.h ** 2 + (self.a / (2 * tan(radians(180 / self.n)))) ** 2) ** 0.5


class Cylinder(Circle):
    """Цилиндр."""
    r: float
    h: float

    def __init__(self, r: float, h: float) -> None:
        super().__init__(r)
        self.h = h

    def side_area(self) -> float:
        """Вычисление площади боковой поверхности."""
        return self.perimeter() * self.h

    def total_area(self) -> float:
        """Вычисление полной площади."""
        return self.side_area() + self.area() * 2

    def volume(self) -> float:
        """Вычисление объема."""
        return self.area() * self.h


class Cone(Circle):
    """Конус."""
    r: float
    h: float

    def __init__(self, r: float, h: float) -> None:
        super().__init__(r)
        self.h = h

    def total_area(self) -> float:
        """Вычисление полной площади."""
        return self.side_area() + self.area()

    def axial_area(self) -> float:
        """Вычисление площади осевого сечения."""
        return self.diameter() * self.h / 2

    def side_area(self) -> float:
        """Вычисление площади боковой поверхности."""
        return pi * self.r * self.line()

    def line(self) -> float:
        """Вычисление образующей конуса."""
        return (self.h ** 2 + self.r ** 2) ** 0.5

    def volume(self) -> float:
        """Вычисление объема."""
        return (pi * self.r ** 2 * self.h) / 3
