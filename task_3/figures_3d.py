from math import pi
from abstract_figures import Figure
import figures_2d


class Sphere(figures_2d.Circle):
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


class Cube(figures_2d.Square): #TODO описать класс
    """Куб."""
    x: float

    def __init__(self, x: float) -> None:
        super().__init__(x)

    def area(self) -> float:
        return 6 * self.x ** 2

    def perimeter(self) -> float:
        return self.x * 12


class Parallelepiped(Figure): #TODO описать класс
    """Параллелепипед."""
    pass


class Pyramid(Figure): #TODO описать класс
    """Пирамида."""
    pass


class Cylinder(figures_2d.Circle): #TODO описать класс
    """Цилинд."""
    pass


class Cone(Figure): #TODO описать класс
    """Конус."""
    pass
