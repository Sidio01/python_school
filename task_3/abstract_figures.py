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
    #TODO добавить метод "нарисовать" (draw)
    

# #TODO возможно дубляж, удалить
# class Figure_2D(Figure):
#     """Плоская фигура."""
#     @abc.abstractmethod
#     def area(self):
#         """Расчет площади."""
#         pass
    
#     @abc.abstractmethod
#     def perimeter(self):
#         """Расчет периметра."""
#         pass

# class Figure_3D(Figure):
#     """Объемная фигура."""
#     @abc.abstractmethod
#     def area(self):
#         """Расчет площади."""
#         pass
    
#     @abc.abstractmethod
#     def perimeter(self):
#         """Расчет периметра."""
#         pass