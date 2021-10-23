import abc


class Figure(abc.ABC):
    """Абстрактная фигура."""
    @abc.abstractmethod
    def area(self):
        """Абстрактный метод - Расчет площади."""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """Абстрактный метод - Расчет периметра."""
        pass
