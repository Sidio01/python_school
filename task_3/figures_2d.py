from math import cos, pi, sin, degrees
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
    a: float

    def __init__(self, a: float) -> None:
        self.a = a

    def area(self) -> float:
        """Вычисление площади."""
        return self.a ** 2

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self.a * 4

    def diagonal(self) -> float:
        """Вычисление длины диагонали."""
        return 2 ** 0.5 * self.a


class Rectangle(Square):
    """Прямоугольник."""
    a: float
    b: float

    def __init__(self, a: float, b: float) -> None:
        super().__init__(a)
        self.b = b

    def area(self) -> float:
        """Вычисление площади."""
        return self.a * self.b

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return (self.a + self.b) * 2

    def diagonal(self) -> float:
        """Вычисление длины диагонали."""
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def radius(self) -> float:
        """Вычисление радиуса описанной окружности."""
        return (self.a ** 2 + self.b ** 2) ** 0.5 / 2


class Triangle(Figure):
    """Треугольник."""
    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Вычисление площади."""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self.a + self.b + self.c

    def altitude_on_a(self) -> float:
        """Вычисление высоты, опущенной на сторону 'a'."""
        p = self.perimeter() / 2
        return (2 * (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5) / self.a

    def altitude_on_b(self) -> float:
        """Вычисление высоты, опущенной на сторону 'b'."""
        p = self.perimeter() / 2
        return (2 * (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5) / self.b

    def altitude_on_c(self) -> float:
        """Вычисление высоты, опущенной на сторону 'c'."""
        p = self.perimeter() / 2
        return (2 * (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5) / self.c


class Trapezoid(Figure):
    """Трапеция. Основаниями выступают 'а' и 'с'."""
    a: float
    b: float
    c: float
    d: float

    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self) -> float:
        """Вычисление площади."""
        m = self.midsegment()
        return m * (self.a ** 2 - (((self.d - self.b) ** 2 + self.a ** 2 - self.c ** 2) / (2 * (self.d - self.b))) ** 2) ** 0.5

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self.a + self.b + self.c + self.d

    def midsegment(self) -> float:
        """Вычисление средней линии."""
        return (self.b + self.d) / 2


class Rhombus(Square):
    """Ромб."""
    a: float
    h: float

    def __init__(self, a: float, h: float) -> None:
        super().__init__(a)
        self.h = h

    def area(self) -> float:
        """Вычисление площади."""
        return self.a * self.h

    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self.a * 4

    def angle_alpha(self) -> float:
        """Вычисление острого угла."""
        return degrees(sin(self.h / self.a))

    def angle_beta(self) -> float:
        """Вычисление тупого угла."""
        return 180 - self.angle_alpha()

    def diagonal(self) -> float:
        """Вычисление диагонали."""
        return self.a * sin(self.angle_alpha() / 2)

    def reverse_diagonal(self) -> float:
        """Вычисление обратной диагонали."""
        return self.a * cos(self.angle_alpha() / 2)
