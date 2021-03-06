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

#########################################################################
#########################################################################

    @property
    def shape_area(self):
        return 3.14*self._radius**2

##########################################################################
##########################################################################

    def __eq__(self, other):
        if type(other) != Circle:
            return False
        if other._radius == self._radius:
            return True
        return False

    def __gt__(self, other):
        if self._radius > other._radius:
            return True
        return False

    def __lt__(self, other):
        if self._radius < other._radius:
            return True
        return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

##########################################################################
##########################################################################

    def __add__(self, other):
        if type(other) is not Circle:
            raise Exception('Addition is only allowed for Circle objects')
        return Circle(self._inner_color, self._border_color, self._radius + other._radius)

    def __sub__(self, other):
        if type(other) is not Circle:
            raise Exception('Subtraction is only allowed for Circle objects')
        if self._radius - other._radius <= 0:
            raise Exception('New value of the Radius should not be less than 0')
        return Circle(self._inner_color, self._border_color, self._radius - other._radius)

    def __mul__(self, other):
        if type(other) not in [Circle,int, float]:
            raise Exception('Multiplications is only allowed for Circle and number objects')
        if type(other) in [int, float]:
            return Circle(self._inner_color, self._border_color, self._radius * other)
        return Circle(self._inner_color, self._border_color, self._radius * other._radius)

###########################################################################
###########################################################################
    def __str__(self):
        try:
            return f"{type(self).__name__} has radius of {self._radius} with inner color {self._inner_color} and with border color {self._border_color} "
        except Exception as excpt:
            return f'Attributes are missing, return of value is not possible due to {excpt}'

if __name__ == '__main__':
    b= Circle('red', 'green',5)
    print(b)
    b.set_radius(10)
    print(b)
    print(b.get_radius())
    print(b.shape_area)

    c =Circle('red', 'green',15)
    d =Circle('red', 'white',20)
    print(c<=d)
    e = d-c
    print(e)
    f= c*d
    print(f)
    k=c*2
    print(k)

