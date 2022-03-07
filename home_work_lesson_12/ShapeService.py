from Shape import Shape
from Circle import Circle
from Rectangle import Rectangle
from Square import Square


class ShapeService:
    DEFAULT_INNER_COLOR = 'green'
    DEFAULT_OUTER_COLOR = 'white'
    def __init__(self, _inner_color=None, _border_color=None):
        if _inner_color is None:
            self._inner_color = self.DEFAULT_INNER_COLOR
        else:
            self._inner_color = _inner_color
        if _border_color is None:
            self._border_color = self.DEFAULT_OUTER_COLOR
        else:
            self._border_color = _border_color

    def __str__(self):
        try:
            return f'{type(self).__name__} with Inner Color {self._inner_color} and with Border Color {self._border_color}'
        except Exception as excpt:
            return f' Attributes are missing, return of value is not possible due {excpt} '


    @staticmethod
    def create_default_circle(radius):
        new_circle = Circle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_OUTER_COLOR, radius)
        return new_circle

    @staticmethod
    def create_default_rectangle(width, length):
        new_rectangle = Rectangle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_OUTER_COLOR, width, length)
        return new_rectangle

    @staticmethod
    def create_default_square(side_length):
        new_square = Square(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_OUTER_COLOR, side_length)
        return new_square

    @staticmethod
    def color_shapes(list_of_shapes, new_inner_color, new_border_color):
        # new_shapes_list = []
        for shape in list_of_shapes:
            shape._inner_color = new_inner_color
            shape._border_color = new_border_color
            # new_shapes_list.append(shape)
        return list_of_shapes



a = ShapeService.create_default_circle(14)
print(a)

b = ShapeService.create_default_rectangle(5,15)
print (b)


c1 = Circle("red", "blue", 5)
c2 = Circle("yellow", "olive", 4)
r1 = Rectangle("red", "blue", 5, 4 )
r2 = Rectangle("black", "white", 20, 33)
s1 = Square("red", "white", 4)
s2 = Square("brown", "blue", 25)

list_of_shapes = [c1, c2, r1, r2, s1, s2]
ShapeService.color_shapes(list_of_shapes, "black", "green")

for shape in list_of_shapes:
    print(shape)

