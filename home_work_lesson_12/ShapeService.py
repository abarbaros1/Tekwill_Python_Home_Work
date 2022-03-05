import Shape
import Circle
import Rectangle
import Square


class ShapeService:
    def __init__(self, _inner_color=None, _border_color=None):
        if _inner_color is None:
            self._inner_color = self.default_inner_color
        else:
            self._inner_color = _inner_color
        if _border_color is None:
            self._border_color = self.default_border_color
        else:
            self._border_color = _border_color

    def __str__(self):
        try:
            return f'{type(self).__name__} with Inner Color {self._inner_color} and with Border Color {self._border_color}'
        except Exception as excpt:
            return f' Attributes are missing, return of value is not possible due {excpt} '


    @property
    def default_inner_color(self):
        return 'white'

    @property
    def default_border_color(self):
        return 'black'

    @staticmethod
    def create_default_circle(radius):
        new_circle = Circle(ShapeService.default_inner_color, ShapeService.default_border_color, radius)
        return new_circle



x = ShapeService()
print(x)

y = create_default_circle(5)
print(z)
