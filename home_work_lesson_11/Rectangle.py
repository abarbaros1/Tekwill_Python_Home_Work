from Shape import Shape

class Rectangle(Shape):
    def __init__(self,_inner_color,_border_color, _width, _length):
        super().__init__(_inner_color,_border_color)
        self._width = _width
        self._length = _length
    def __str__(self):
        return f"{type(self).__name__} has width {self._width} and length {self._length}, with inner color {self._inner_color} and border color {self._border_color} "

a=Rectangle('red', 'green', 4,5)
print(a)