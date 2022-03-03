from Shape import Shape

class Circle(Shape):

    def __init__(self, _inner_color=None,_border_color=None,_radius=None):
        super().__init__(_inner_color,_border_color)
        self._radius = _radius

    def set_radius(self,_radius=None):
        self._radius = _radius
        return self

    def get_radius(self):
        return self._radius

    def __str__(self):
        try:
            return f"{type(self).__name__} has radius of {self._radius} with inner color {self._inner_color} and with border color {self._border_color} "
        except Exception as excpt:
            return f'Attributes are missing, return of value is not possible due to {excpt}'


# b= Circle('red', 'green',5)
# print(b)
# b.set_radius(10)
# print(b)
# print(b.get_radius())


