from Shape import Shape

class Circle(Shape):

    def __init__(self, _inner_color,_border_color,_radius):
        super().__init__(_inner_color,_border_color)
        self._radius = _radius

    def get_radius(self,_radius):
        self._radius = _radius
        return self

    def __str__(self):
        try:
            return f"{type(self).__name__} has radius of {self.radius} with inner color {self.inner_color} and with border color {self.border_color} "
        except Exception as excpt:
            return f'Attributes are missing, return of value is not possible due to {excpt}'


# b= Circle('red', 'green',5)
# print(b)
# b.get_radius(10)
# print(b)


