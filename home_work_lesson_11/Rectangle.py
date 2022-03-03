from Shape import Shape

class Rectangle(Shape):
    def __init__(self,_inner_color,_border_color, _width, _length):
        super().__init__(_inner_color,_border_color)
        self._width = _width
        self._length = _length

    def set_width(self,_width):
        self._width = _width
        return self

    def get_width(self):
        return self._width

    def set_length(self,_length):
        self._length = _length
        return self

    def get_length(self):
        return self._length


    def __str__(self):
        return f"{type(self).__name__} has width {self._width} and length {self._length}, with inner color {self._inner_color} and border color {self._border_color} "

# a=Rectangle('red', 'green', 4,5)
# print(a)
# a.set_width(10)
# print(a)
# print(a.get_width())
