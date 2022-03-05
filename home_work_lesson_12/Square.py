from Rectangle import Rectangle
from Circle import Circle

class Square(Rectangle):
    def __init__(self,_inner_color,_border_color, _length):
        super().__init__(_inner_color,_border_color,_length, _length)

    def set_width(self,_width):
        self._width = _width
        self._length = _width
        # return self

    def set_length(self,_length):
        self._length = _length
        self._width = _length
        # return self

    def __str__(self):
        return f"{type(self).__name__} has width {self._width} and length {self._length}, with inner color {self._inner_color} and border color {self._border_color} "

if __name__ == '__main__':
    a=Square('red', 'green', 4)
    print(a)
    a.set_width(10)
    print(a)
    print(a.get_width())
    a.set_length(15)
    print(a)
    print(a.shape_area)

    b = Rectangle('red', 'green', 15,15)
    c = Square('red', 'green', 14)
    d = Circle('red', 'green', 5)
    print(b<=c)
    print(b<d)

    e = b-c
    print(e)
    f = c*2
    print(f)