from Shape import Shape
from Circle import Circle

class Rectangle(Shape):
    def __init__(self,_inner_color,_border_color, _width, _length):
        super().__init__(_inner_color,_border_color)
        self._width = _width
        self._length = _length

    def set_width(self,_width):
        self._width = _width
        # return self

    def get_width(self):
        return self._width

    def set_length(self,_length):
        self._length = _length
        # return self

    def get_length(self):
        return self._length
###################################################################################
###################################################################################
    @property
    def shape_area(self):
        return self._length*self._width
####################################################################################
####################################################################################


    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        if other._length * other._width == self._length * self._width:
            return True
        return False


    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return False
        if self._length * self._width > other._length * other._width:
            return True
        return False


    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return False
        if self._length * self._width < other._length * other._width:
            return True
        return False


    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self == other or self < other


    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self == other or self > other
####################################################################################
####################################################################################

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise Exception('Addition is only allowed for Rectangle objects')
        return Rectangle(self._inner_color, self._border_color, self._width + other._width, self._length + other._length)


    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise Exception('Subtraction is only allowed for Rectangle objects')
        if (self._width - other._width) <=0:
            raise Exception('New value of the Width should not be less than 0')
        if (self._length - other._length) <=0:
            raise Exception('New value of the Length should not be less than 0')
        return Rectangle(self._inner_color, self._border_color, self._width - other._width, self._length - other._length)


    def __mul__(self, other):
        if type(other) not in [Rectangle, int, float]:
            raise Exception('Subtraction is only allowed for Rectangle and number objects')
        if type(other) in [int, float]:
            return Rectangle(self._inner_color,self._border_color, self._width * other, self._length * other)
        return Rectangle(self._inner_color,  self._border_color, self._width * other._width, self._length * other._length)


####################################################################################
####################################################################################
    def __str__(self):
        return f"{type(self).__name__} has width {self._width} and length {self._length}, with inner color {self._inner_color} and border color {self._border_color} "

if __name__ == '__main__':
    a=Rectangle('red', 'green', 4,5)
    print(a)
    a.set_width(10)
    print(a)
    print(a.get_width())
    print(a.shape_area)

    b = Rectangle('red', 'green', 10,2)
    c = Rectangle('red', 'green', 5,10)
    d = Circle('red', 'green', 5)
    print(b<=c)
    print(b==d)

    e = b*c
    print(e)
    f = c*10
    print(f)
