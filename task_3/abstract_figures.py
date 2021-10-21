import abc


class Figure(abc.ABC):
    """Фигура."""
    @abc.abstractmethod
    def area(self):
        """Расчет площади."""
        pass
    
    @abc.abstractmethod
    def perimeter(self):
        """Расчет периметра."""
        pass

#TODO возможно дубляж, удалить
class Figure_2D(Figure):
    """Плоская фигура."""
    @abc.abstractmethod
    def area(self):
        """Расчет площади."""
        pass
    
    @abc.abstractmethod
    def perimeter(self):
        """Расчет периметра."""
        pass

class Figure_3D(Figure):
    """Объемная фигура."""
    @abc.abstractmethod
    def area(self):
        """Расчет площади."""
        pass
    
    @abc.abstractmethod
    def perimeter(self):
        """Расчет периметра."""
        pass