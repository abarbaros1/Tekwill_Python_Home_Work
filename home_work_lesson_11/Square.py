from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,_inner_color,_border_color, _length):
        super().__init__(_inner_color,_border_color,_length, _length)
        self._width = _length
        self._length = _length

    def set_width(self,_width):
        self._width = _width
        self._length = _width
        # return self

    def get_width(self):
        return self._width

    def set_length(self,_length):
        self._length = _length
        self._width = _length
        # return self

    def get_length(self):
        return self._length

    def __str__(self):
        return f"{type(self).__name__} has width {self._width} and length {self._length}, with inner color {self._inner_color} and border color {self._border_color} "

# a=Square('red', 'green', 4)
# print(a)
# a.set_width(10)
# print(a)
# print(a.get_width())
# a.set_length(15)
# print(a)
